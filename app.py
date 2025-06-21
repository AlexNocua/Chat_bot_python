from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_admin import Admin
import os

# instancia de la base de datos para el gerenciamiento total y ajustes de los modelos
db = SQLAlchemy()

##########################################################
# # prueba de ejecucion de flask
# app = Flask(__name__)


# @app.route("/")
# def prueba():
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
##########################################################

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "database.db")}'
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    return app

    # importante probar lo siguiente:
    #     from app.models import User, WhatsAppGroup
    #     User.query.all()
    # # Debe devolver una lista vacía (sin errores)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
