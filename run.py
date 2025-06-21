from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_admin import Admin
import os



# prueba de ejecucion de flask
app = Flask(__name__)

@app.route("/")
def prueba():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug = True, port=5000)



# db = SQLAlchemy()
# login_manager = LoginManager()

# def create_app():
#     app = Flask(__name__)
    
#     # Configuración
#     app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
#     app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    
#     # Inicializar extensiones
#     db.init_app(app)
#     login_manager.init_app(app)
    
#     # Registrar blueprints
#     from app.routes import main_bp, auth_bp
#     app.register_blueprint(main_bp)
#     app.register_blueprint(auth_bp)
    
#     # Configurar admin
#     from app.admin import setup_admin
#     setup_admin(app)
    
#     # Iniciar WhatsApp bot en segundo plano
#     from app.whatsapp.sender import start_whatsapp_bot
#     start_whatsapp_bot(app)
    
#     return app