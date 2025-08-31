from flask import Flask
import os
from app.routes import *  # Importar TODOS los blueprint
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    login_manager_app = LoginManager(app)

    @login_manager_app.user_loader
    def load_user(id):
        return ModelUser.get_by_id(id)
    
    csrf = CSRFProtect()
    app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))
    # Configuraciones (BD, blueprints, etc.)
    app.register_blueprint(home)
    app.register_blueprint(debug_bp)
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    return app
