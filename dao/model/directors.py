from marshmallow import fields, Schema
from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

    def __str__(self):  # Не понял, как это работает, погуглить
        return self.name
