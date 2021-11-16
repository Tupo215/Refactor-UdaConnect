from models import Location
from geoalchemy2.types import Geometry as GeometryType
from marshmallow import Schema, fields
from marshmallow_sqlalchemy.convert import ModelConverter as BaseModelConverter


class LocationSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer()
    creation_time = fields.DateTime()
    latitude = fields.String()
    longitude = fields.String()
    coordinate = fields.String()

    class Meta:
        model = Location