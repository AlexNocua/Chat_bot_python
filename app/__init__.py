from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "database.db")}'

    db.init_app(app)
    login_manager.init_app(app)

    # Importación del modelo User para registrar el cargador de usuarios
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Rutas y admin
    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.admin import setup_admin
    setup_admin(app)

    # Crear las tablas
    with app.app_context():
        db.create_all()

    return app
