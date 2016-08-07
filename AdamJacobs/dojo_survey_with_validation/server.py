from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'sexyorange'

name = None
location = None
@app.route('/')
def index():
 	return render_template('index.html')

@app.route('/results', methods = ['POST'])
def create_student():
  	name = request.form['name']
  	if len(name) < 1:
  		flash('Name cannot be empty!')
  	else:
  		flash('{}'.format(name))
  	location = request.form['location']
  	language = request.form['language']
  	if request.form['comment']:
  		comment = request.form['comment']
  	else:
  		comment = None
  	print name
  	print location
  	print language
  	if request.form['comment']:
  		print comment
  	return render_template('result.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

app.run(debug=True)
