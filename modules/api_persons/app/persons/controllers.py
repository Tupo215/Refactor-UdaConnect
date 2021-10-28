from datetime import datetime

from app.persons.models import Person
from app.persons.schemas import PersonSchema
from app.persons.services import PersonService
from flask import request, jsonify
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("persons", description="Connections via geolocation.")  # noqa


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return jsonify(person)