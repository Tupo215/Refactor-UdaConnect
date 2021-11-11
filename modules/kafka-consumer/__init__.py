import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json


from app.models import Location
from app.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
import psycopg2
import app.controllers

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-api")

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

# kafka consumer message
kafka_consumer = app.controllers.g.kafka_consumer

for message in kafka_consumer:
    msg = json.loads((message.value.decode('utf-8'))
    if 'coordinate'in msg:
        LocationService.retrieve(msg)
    else:
        logging.warning('No coordinate provided')