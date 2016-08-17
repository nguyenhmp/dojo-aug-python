from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'bananas2'

@app.route('/')
def index():
	session.setdefault('secretnum', random.randrange(0,101))
	session.setdefault('guess', '')
	print session['secretnum'], type(session['secretnum'])
	print session['guess'], type(session['guess'])
	return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
	session['guess'] = int(request.form['guess'])
	return redirect('/')

@app.route('/refresh', methods=['POST'])
def try_again():
	session.clear()
	return redirect('/')

app.run(debug=True)