from flask import Flask

app = Flask(__name__)
# A Secret key should be created to use flash message
app.secret_key = '6kjljhoi0p'

if __name__ == '__main__':
	app.run(debug=True)
