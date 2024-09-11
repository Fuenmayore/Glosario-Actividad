from flask import Flask
from app.controllers.user_controller import user_blueprint

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(user_blueprint)
    
    return app
