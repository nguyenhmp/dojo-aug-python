from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'banana'

def sumSessionCounter():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 0

@app.route('/')
def index():
	sumSessionCounter()
 	return render_template('index.html', counter = session['counter'])

@app.route('/clear', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')

@app.route('/iterate', methods=['POST'])
def iterate():
	print "yay"
	session['counter']+=1
	return redirect('/')

app.run(debug=True)


