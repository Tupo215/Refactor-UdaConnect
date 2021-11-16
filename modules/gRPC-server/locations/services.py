import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json
import grpc
import create_locations_pb2
import create_locations_pb2_grpc
from locations.models import Location
from locations.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
import psycopg2
import locations.controllers

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

channel = grpc.insecure_channel("localhost:30003")
stub = create_locations_pb2_grpc.LocationServiceStub(channel)

class LocationService:
    @staticmethod
    def retrieve(location_id):
        # query the database to get location based on location_id
        location = locations.controllers.db.session.query(Location, Location.coordinate.ST_AsText()).filter(Location.id == location_id).one()
        # send data to kafka
        kafka_data = json.dumps(location).encode()
        kafka_producer = locations.controllers.g.kafka_producer
        kafka_producer.send("locations", kafka_data)
        
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        
        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.latitude = location["latitude"] 
        new_location.longitude = location["longitude"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        
        # connects to the gRPC server and uses location service defined in __init__.py
        new__location = stub.Create(create_locations_pb2.LocationMessage(
        id = new_location.id,
        person_id = new_location.person_id,
        creation_time = new_location.creation_time,
        latitude = new_location.latitude,
        longitude = new_location.longitude))

        return new__location