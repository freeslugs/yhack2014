from mongoengine import StringField, DecimalField, ReferenceField, ListField, DictField

from app import db

#class Image(db.Document):
#	tag = StringField(required=True)
#	prob = DecimalField(required=True, precision=10)


class Movie(db.Document):
	name = StringField(required=True, unique=True)
	imgs = ListField(DictField())
