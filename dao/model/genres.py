from marshmallow import fields, Schema
from setup_db import db


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):  # Не понял, как это работает, погуглить
        return self.name
