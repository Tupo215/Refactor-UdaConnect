from datetime import datetime
import logging
from flask_sqlalchemy import SQLAlchemy

import flask
from kafka import KafkaProducer, KafkaConsumer
from locations.models import Location
from locations.schemas import LocationSchema
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import locations.services
import grpc
import create_locations_pb2
import create_locations_pb2_grpc

DATE_FORMAT = "%Y-%m-%d"

api = Flask(__name__)
#connect to database
api.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://localhost:5432/geoconnections'

db = SQLAlchemy(api)

logging.basicConfig(level=logging.DEBUG )

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
        location = locations.services.LocationService.retrieve(location_id)
        return jsonify(location)
    elif request.method == 'POST':
        request.get_json()
        location = stub.Create(create_locations_pb2.LocationMessage(request.get_json))
        return jsonify(location)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == "__main__": 
   api.run(host='0.0.0.0', port='30002')