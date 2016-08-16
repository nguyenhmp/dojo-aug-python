from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return 'No Ninjas Here!'

@app.route('/ninjas')
def show_all():
	return render_template('process.html')

@app.route('/ninjas/<color>')
def show_ninja(color): 		
	return render_template('index.html', color=color)
	
app.run(debug=True)