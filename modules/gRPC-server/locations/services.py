import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json


from models import Location
from schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
import psycopg2
import controllers

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

class LocationService:
    @staticmethod
    def retrieve(location_id):
        # query the database to get location based on location_id
        location = controllers.db.session.query(Location, Location.coordinate.ST_AsText()).filter(Location.id == location_id).one()
        # send data to kafka
        kafka_data = json.dumps(location).encode()
        kafka_producer = controllers.g.kafka_producer
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
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        
        controllers.db.session.add(new_location)
        controllers.db.session.commit()
        return new_location