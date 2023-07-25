from flask import Flask
from urlshort.urlshort import urlshort_bp

app = Flask(__name__)
# A Secret key should be created to use flash message
app.secret_key = '6kjljhoi0p'
app.register_blueprint(urlshort_bp)


if __name__ == '__main__':
	app.run(debug=True)
