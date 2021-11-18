import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json

import app.controllers
from app.models import Location
from app.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
import psycopg2
from kafka import KafkaConsumer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'localhost:9092'
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
class LocationService:
    @staticmethod
    def retrieve(location_id):
        # query database to get location based on location_id
        location = app.controllers.db.session.query(Location, Location.coordinate.ST_AsText()).filter(Location.id == location_id).one()
        
        return location
a = 1

while a==1:
    # kafka consumer message
    kafka_consumer = consumer

    for message in kafka_consumer:
        msg = json.loads(message.value.decode('utf-8'))
        if 'coordinate' in msg:
            LocationService.retrieve(msg)
        else:
            logging.warning('No coordinate provided')

