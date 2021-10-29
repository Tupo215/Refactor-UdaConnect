from datetime import datetime
import logging
from kafka import KafkaProducer
from app.locations.models import Location
from app.locations.schemas import LocationSchema
from app.locations.services import LocationService
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("locations", description="Connections via geolocation.")  # noqa

logging.basicConfig(level=logging.DEBUG )

@api.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer

@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return jsonify(location)

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return jsonify(location)