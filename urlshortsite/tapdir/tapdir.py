from flask import Flask, Blueprint


tapdir_bp = Blueprint('tapdir', __name__)

@tapdir_bp.route('/')
def home():
	return "hi home"


if __name__ == '__main__':
	tapdir_bp.run(debug=True)
