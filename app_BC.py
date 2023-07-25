from flask import Flask
from .urlshort.urlshort import urlshort_bp

def create_app():
    app = Flask(__name__)
    # A Secret key should be created to use flash message
    app.secret_key = '6kjljhoi0p'
    app.register_blueprint(urlshort_bp)
    return app
