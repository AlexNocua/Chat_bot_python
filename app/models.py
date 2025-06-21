# Creacion de la base de datos

# importaciones
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100), primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)


class WhatsAppGroup(db.model):
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(50))
    invite_link = db.Column(db.String(200), primary_key=True)
    is_active = db.Column(db.Boolean, default=False)


class Campaing(db.model):
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(100))
    message_template = db.Column(db.Text)
    target_group_id = db.Column(db.Integer, db.ForeingKey("Whatsapp_group.id"))
    is_running = db.Column(db.Boolean, default=False)
