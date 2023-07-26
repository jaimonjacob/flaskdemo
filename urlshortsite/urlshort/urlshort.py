from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
import os
from werkzeug.utils import secure_filename

urlshort_bp = Blueprint('urlshort', __name__, static_folder='static', static_url_path='urlshort/static', template_folder='templates')

@urlshort_bp.route('/')
def home():
	return render_template('home.html', shortnames = session.keys())

@urlshort_bp.route('/your-url', methods = ['GET', 'POST'])
def your_url():
	if request.method=='POST':
		cwd = os.getcwd()
		files = os.listdir(cwd)  # Get all the files in that directory
		print("Files in %r: %s" % (cwd, files))
		urls = {}
		# Check if the file exists, and if yes, convert to json and assign to a variable
		if os.path.exists('urlshortsite/urlshort/url.json'):
			with open('urlshortsite/urlshort/url.json',) as url_file_object:
				urls = json.load(url_file_object)
		
		# Check if the current shortname, exists in the json. if yes, flas a message and redirect to home
		if request.form['shortname'] in urls.keys():
			flash('This entry already exists; please use a new entry')
			return redirect(url_for('urlshort.home'))
		
		if 'inputurl' in request.form.keys():
			# Collect the shortname and url from the form and add to the 'urls' object
			urls[request.form['shortname']] = {'url' :  request.form['inputurl']}
		else:
			# assign the uploaded file to a variable
			f = request.files['file']
			# create a file that is a combination of the shortcode and the uploaded file name
			full_name = request.form['shortname'] + '_' + f.filename
			# save the file to the current directory with the full name added to the file name
			f.save('urlshort/static/user_files/'+ full_name)
			# Collect the shortname and filename  and add to the 'urls' object
			urls[request.form['shortname']] = {'file' :  secure_filename(full_name)}
			# Open the file and add the object to the json file
		with open('urlshortsite/urlshort/url.json', 'w') as url_file_object:
			json.dump(urls, url_file_object)
			# Adding to a cookie
			session[request.form['shortname']] = True
		return render_template('your_url.html', inputtext = request.form['shortname'])
	
	else:
		# if the method is not post, redirect to home
		return redirect(url_for('urlshort.home'))

# Dynamic varialbe assignments 
@urlshort_bp.route('/<string:code>')
def redirect_to_url(code):
	if os.path.exists('urlshortsite/urlshort/url.json'):
		with open('urlshortsite/urlshort/url.json') as url_file_object:
				urls = json.load(url_file_object)
				if code in urls.keys():
					# if the code is in the json file, then go to the url address relevant to the code
					if 'url'in urls[code].keys():
						return redirect(urls[code]['url'])
					else:
					# if the code is in the json, then go to the url address for the file relevant to the code. url_for function is needed to generate urls for files						
						return redirect(url_for('urlshort.static', filename='user_files/' + urls[code]['file']))
	return abort(404)


# Adding a custom 404 page
@urlshort_bp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

# Creating API
@urlshort_bp.route('/api')
def convert_api():
	return jsonify(list(session.keys()))

if __name__ == '__main__':
	urlshort_bp.run(debug=True)
