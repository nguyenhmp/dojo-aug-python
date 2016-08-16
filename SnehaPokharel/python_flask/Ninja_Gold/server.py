from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)
app.secret_key = 'Monday'
import random
import datetime

@app.route('/')
def home():
	if 'gold' in session:
		pass 
	else:
		session['gold'] = 0

	session['date']= datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)") 
	
	if 'list' in session: # we need to create a list to add into the activity log. updates every time you add the string variable. 
		pass 
	else:
		session['list'] = []
	
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def count():

	type(request.form['building'])
	if request.form['building'] == "farm":
		session['gold']= session['gold'] + random.randrange(10, 21) # 
		session['saying'] = str("Earned ") + str(session['gold']) + str(" golds from the farm! ") + str(session['date']) #printing to the log
		session['list'].append({'text': session['saying'], 'color': 'green'}) # you need to create a dictionary for the color value
	elif request.form['building'] == "cave":
		session['gold']= session['gold'] + random.randrange(5,11)
		session['saying'] = str("Earned ") + str(session['gold']) + str(" golds from the cave! ") + str(session['date'])
		session['list'].append({'text': session['saying'], 'color': 'green'})
	elif request.form['building'] == "house":
		session['gold']= session['gold'] + random.randrange(2,6)
		session['saying'] = str("Earned ") + str(session['gold']) + str(" golds from the house! ") + str(session['date'])
		session['list'].append({'text': session['saying'], 'color': 'green'})
	elif request.form['building'] == "casino":
			session['gold'] = session['gold'] + random.randrange(-50,51)
			if session['gold'] > 0: 
				session['saying'] = str("Entered a casino and won ") + str(session['gold']) + str(" golds from the casino!")
				session['list'].append({'text': session['saying'], 'color': 'green'})
			else:
				session['saying'] = str("Entered a casino and lost ") + str(session['gold']*-1) + str(" golds... OUCHY!..") + str(session['date'])
				session['list'].append({'text': session['saying'], 'color': 'red'})


	print session['list']	

	return redirect('/') 
	
@app.route('/reset', methods=['GET'])
def reset():	
	session.clear()
	return redirect('/')

app.run(debug=True)