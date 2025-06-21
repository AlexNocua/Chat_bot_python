# Creacion de la base de datos

# importaciones
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)


class WhatsAppGroup(db.Model):
    __tablename__ = 'whatsapp_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    invite_link = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=False)


class Campaign(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    message_template = db.Column(db.Text)
    target_group_id = db.Column(db.Integer, db.ForeignKey('whatsapp_group.id'))
    is_running = db.Column(db.Boolean, default=False)
