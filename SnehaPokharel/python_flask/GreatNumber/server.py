from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)
app.secret_key = 'boom'

import random 

@app.route('/')
def home():
	if 'rando' in session:
		pass  
	else:
		session['rando'] = random.randrange(0, 101) 
	print session['rando']
	return render_template('index.html')
	# if session rando has not been set, set the random number, if the number has been set, leave it alone.

@app.route('/process', methods=['POST'])
def boom():
	type(request.form['choice'])
	
	if session['rando'] == int(request.form['choice']): # if the guessed number and random number are equal
		session['result'] = "match"

	elif session['rando'] > int(request.form['choice']):
		session['result'] = "low"
	
	else:
		session['result'] = "high"

		# session['result'] == "high"
	# no matter what, redirect to index function	
	return redirect('/') 
	
@app.route('/reset', methods=['GET'])
def reset():	
	session.clear()
	session['number'] = random.randrange(0, 101)
	return redirect('/')

app.run(debug=True)