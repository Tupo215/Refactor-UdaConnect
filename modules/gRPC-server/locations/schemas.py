from locations.models import Location
from geoalchemy2.types import Geometry as GeometryType
from marshmallow import Schema, fields
from marshmallow_sqlalchemy.convert import ModelConverter as BaseModelConverter


class LocationSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer()
    coordinate = fields.String()
    latitude = fields.String()
    longitude = fields.String()
    creation_time = fields.DateTime()

    class Meta:
        model = Location