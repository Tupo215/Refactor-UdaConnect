from datetime import datetime
import logging
from config import config_by_name
import flask
from flask_sqlalchemy import SQLAlchemy
from kafka import KafkaProducer, KafkaConsumer
from models import Location
from schemas import LocationSchema
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import services
import grpc
import create_locations_pb2
import create_locations_pb2_grpc

DATE_FORMAT = "%Y-%m-%d"

api = Flask(__name__)
env=None
#connect to database
api.config.from_object(config_by_name[env or "dev"])

#init database
db = SQLAlchemy(api)

# set up logging
logging.basicConfig(level=logging.DEBUG )

#connect to grpc-server
channel = grpc.insecure_channel("localhost:30003")
stub = create_locations_pb2_grpc.LocationServiceStub(channel)

@api.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    consumer = KafkaConsumer(TOPIC_NAME)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer
    g.kafka_consumer = consumer

@api.route("/locations/<location_id>", methods=['GET', 'POST'])
def locations(location_id):
    if request.method == 'GET':
        # call the location service to retrieve location according to location id and send data to 
        # kafka 
        location = services.LocationService.retrieve(location_id)
        return jsonify(location)
    elif request.method == 'POST':
        request.get_json()
        # call the location service which calls the grpc server to send the new location
        location = services.LocationService.create(request.get_json)
        return jsonify(location)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == "__main__": 
   api.run(host='0.0.0.0', port='5001')