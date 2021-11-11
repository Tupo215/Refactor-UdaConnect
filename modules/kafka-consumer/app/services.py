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
import grpc
import create_locations_pb2
import create_locations_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

# connect to gRPC server
channel = grpc.insecure_channel("localhost:30003")
stub = create_locations_pb2_grpc.LocationServiceStub(channel)

# connect to database
conn = psycopg2.connect("dbname=geoconnections user=ct_admin")
cur = conn.cursor()

class LocationService:
    @staticmethod
    def retrieve(location_id):
        cur.execute("SELECT id, person_id, creation_time, coordinate FROM location WHERE id = %s", (location_id,))
        rows = cur.fetchall()
        for r in rows:
           location = {
                "id" : r[0],
                "person_id" : r[1],
                "creation_time" : str(r[2]),
                "coordinate" : r[3]
                }
        
        cur.close()
        conn.close()
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
        
        # connects to the gRPC server and uses location service defined in __init__.py
        new__location = stub.Create(create_locations_pb2.LocationMessage(
        id = new_location.id,
        person_id = new_location.person_id,
        creation_time = new_location.creation_time,
        coordinate = new_location.coordinate))
        
        return new__location       