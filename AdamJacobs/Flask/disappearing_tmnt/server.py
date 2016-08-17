from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'sexyorange'

@app.route('/')
def index():
 	return render_template('index.html')

@app.route('/ninjas')
def main_ninjas():
  	return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninjas(color):
	print color
  	return render_template('ninjas.html', color=color)
app.run(debug=True)
