from mongoengine import StringField, DecimalField, ReferenceField, ListField

from app import db

class Tag(db.Document):
	tag_id = StringField(required=True)
	prob = DecimalField(required=True, precision=10)


class Movie(db.Document):
	name = StringField(required=True)
	tags = ListField(ReferenceField(Tag))
