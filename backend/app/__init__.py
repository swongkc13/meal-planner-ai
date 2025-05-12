# app/__init__.py

from flask import Flask
from flask_cors import CORS  # ← Import this
from app.routes import recommend_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  
    app.register_blueprint(recommend_bp)
    return app
