from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/your-url', methods = ['GET', 'POST'])
def your_url():
	if request.method=='POST':
		urls = {}
		urls[request.form['shortname']] = {'url' :  request.form['inputurl']}
		with open('url.json', 'w') as url_file_object:
			json.dump(urls, url_file_object)
		return render_template('your_url.html', inputtext = request.form['shortname'])
	else:
		return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)
