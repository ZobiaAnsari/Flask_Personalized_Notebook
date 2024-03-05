# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(20))
    # notes = db.Column(db.String(200))
    notes = db.relationship('Notes', backref = 'user',lazy=True)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    note = db.Column(db.Text(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))