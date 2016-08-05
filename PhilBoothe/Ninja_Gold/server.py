from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key = 'illuminaughty'

@app.route('/')
def index():
	session.setdefault('gold', 0)
	session.setdefault('activity', [])
	return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def cha_ching():

	if request.form['building'] == 'Farm':
		incriment = randint(10, 20)
		session['gold'] += incriment
		activityText = 'Earned ' + str(incriment) + ' gold from the Farm! (' + datetime.now().strftime("%Y/%m/%d %I:%M%p") + ')'
		session['activity'].insert(0, { 'text': activityText, 'class': 'green' })
	elif request.form['building'] == 'Cave':
		incriment = randint(5,10)
		session['gold'] += incriment
		activityText = 'Earned ' + str(incriment) + ' gold from the Cave! (' + datetime.now().strftime("%Y/%m/%d %I:%M%p") + ')'
		session['activity'].insert(0, { 'text': activityText, 'class': 'green' })
	elif request.form['building'] == 'House':
		incriment = randint(2,5)
		session['gold'] += incriment
		activityText = 'Earned ' + str(incriment) + ' gold from the House! (' + datetime.now().strftime("%Y/%m/%d %I:%M%p") + ')'
		session['activity'].insert(0, { 'text': activityText, 'class': 'green' })
	elif request.form['building'] == 'Casino':
		incriment = randint(-50,50)
		session['gold'] += incriment
		if incriment < 0:
			activityText = 'Lost ' + str(int(incriment)*-1) + ' gold at the Casino! Oh no! (' + datetime.now().strftime("%Y/%m/%d %I:%M%p") + ')'
			session['activity'].insert(0, { 'text': activityText, 'class': 'red' })
		else:
			activityText = 'Earned ' + str(incriment) + ' gold at the Casino! (' + datetime.now().strftime("%Y/%m/%d %I:%M%p") + ')'
			session['activity'].insert(0, { 'text': activityText, 'class': 'green' })
	else:
		pass
	return redirect('/')

# @app.route('/reset', methods=['POST'])
# def start_over():
# 	session.clear()
# 	return redirect('/')

app.run(debug=True)