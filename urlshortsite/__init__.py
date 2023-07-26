from flask import Flask
from .urlshort.urlshort import urlshort_bp
from .tapdir.tapdir import tapdir_bp

def create_app(test_config=None):
	app = Flask(__name__)
	# A Secret key should be created to use flash message
	app.secret_key = '6kjljhoi0p'
	app.register_blueprint(urlshort_bp, url_prefix='/')
	app.register_blueprint(tapdir_bp, url_prefix='/tap')
	return app