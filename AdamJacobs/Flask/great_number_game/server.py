from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'sexyorange'

@app.route('/')
def index():
	import random
	session.setdefault('response', 'default')
	session.setdefault('number',0)
	if session['number'] == 0:
		session['number'] = random.randrange(0, 101)
 	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def clear():
	pick = request.form['pick']
	number = session['number']
	pick = int(pick)
	print number
	print pick
	if pick > number:
		session['response'] = 'high'
	if pick < number:
		session['response'] = 'low'
	if pick == number:
		session['response'] = 'same'
	return redirect('/')

@app.route('/again', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)


