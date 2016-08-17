from flask import Flask, render_template, request, redirect
app = Flask(__name__)

name = None
location = None
@app.route('/index.html')
def index():
 	return render_template('index.html')

@app.route('/students', methods = ['POST'])
def create_student():
  if request.method == 'POST':
  	name = request.form['name']
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
