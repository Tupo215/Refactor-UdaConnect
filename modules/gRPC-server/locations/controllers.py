from datetime import datetime
import logging

import flask
from kafka import KafkaProducer, KafkaConsumer
from models import Location
from schemas import LocationSchema
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import services

DATE_FORMAT = "%Y-%m-%d"

api = Flask(__name__)

logging.basicConfig(level=logging.DEBUG )

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
        location = services.LocationService.retrieve(location_id)
        return jsonify(location)
    elif request.method == 'POST':
        request.get_json()
        location = services.LocationService.create(request.get_json())
        return jsonify(location)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == "__main__": 
   api.run(host='0.0.0.0', port='30002')