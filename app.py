from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
# A Secret key should be created to use flash message
app.secret_key = '6kjljhoi0p'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/your-url', methods = ['GET', 'POST'])
def your_url():
	if request.method=='POST':
		urls = {}

		# Check if the file exists, and if yes, convert to json and assign to a variable
		if os.path.exists('url.json'):
			with open('url.json') as url_file_object:
				urls = json.load(url_file_object)
		
		# Check if the current shortname, exists in the json. if yes, flas a message and redirect to home
		if request.form['shortname'] in urls.keys():
			flash('This entry already exists; please use a new entry')
			return redirect(url_for('home'))
		
		if 'inputurl' in request.form.keys():
			# Collect the shortname and url from the form and add to the 'urls' object
			urls[request.form['shortname']] = {'url' :  request.form['inputurl']}
		else:
			# assign the uploaded file to a variable
			f = request.files['file']
			# create a file that is a combination of the shortcode and the uploaded file name
			full_name = request.form['shortname'] + f.filename
			# save the file to the current directory with the full name added to the file name
			f.save('files/'+ full_name)
			# Collect the shortname and filename  and add to the 'urls' object
			urls[request.form['shortname']] = {'file' :  secure_filename(full_name)}
			# Open the file and add the object to the json file
		with open('url.json', 'w') as url_file_object:
			json.dump(urls, url_file_object)
		return render_template('your_url.html', inputtext = request.form['shortname'])
	
	else:
		# if the method is not post, redirect to home
		return redirect(url_for('home'))

# Dynamic varialbe assignments to urls
@app.route('/<string:code>')
def redirect_to_url(code):
	if os.path.exists('url.json'):
		with open('url.json') as url_file_object:
				urls = json.load(url_file_object)
				if code in urls.keys():
					if 'url'in urls[code].keys():
						return redirect(urls[code]['url'])





if __name__ == '__main__':
	app.run(debug=True)
