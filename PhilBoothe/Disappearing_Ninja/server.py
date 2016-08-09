from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return "No ninjas here!"

@app.route('/ninja')
def ninja_home():
	return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_ninja(color):
	if color == 'blue':
		ninja = 'leonardo'
	elif color == 'orange':
		ninja = 'michelangelo'
	elif color == 'red':
		ninja = 'raphael'
	elif color == 'purple':
		ninja = 'donatello'
	else:
		ninja = 'april'
	return render_template('index.html', ninja=ninja)

app.run(debug=True)