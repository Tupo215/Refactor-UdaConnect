import time
from concurrent import futures
import grpc
import create_locations_pb2
import create_locations_pb2_grpc
import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json
import locations.controllers
from locations.models import Location
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
import psycopg2

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

class LocationServicer(create_locations_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location = create_locations_pb2.LocationMessage(
            id = request.id,
            person_id = request.person_id,
            creation_time = request.creation_time,
            latitude = request.latitude,
            longitude = request.longitude)

        new_location = Location()
        new_location.id = location.id
        new_location.person_id = location.person_id
        new_location.creation_time = location.creation_time
        new_location.coordinate = ST_Point(location.latitude, location.longitude)
        
        locations.controllers.db.session.add(new_location)
        locations.controllers.db.session.commit()
        
        return location
        
	    
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
create_locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


# Server starting on port 5005
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)