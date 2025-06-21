from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, WhatsAppGroup, Campaign
from flask_login import current_user
from app import db


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

def setup_admin(app):
    admin = Admin(app, name='WhatsApp Manager', template_mode='bootstrap3')
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(WhatsAppGroup, db.session, name='Grupos'))
    admin.add_view(SecureModelView(Campaign, db.session, name='Campañas'))