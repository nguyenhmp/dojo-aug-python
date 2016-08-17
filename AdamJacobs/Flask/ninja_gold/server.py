from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'sexyorange'

@app.route('/')
def index():
	if 'activities' in session:
		pass
	else:
		session['activities'] = []
	session.setdefault('score',0)
 	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def clear():
	from random import randint
	session['building'] = request.form['building']
	if request.form['building']=='farm':
		from time import gmtime, strftime
		rando = randint(10,20)
		session['score'] += rando
		session['rando'] = rando
		session['building'] = request.form['building']
		session['datetime'] = strftime("%a, %d %b %Y %H:%M", gmtime())
		sentence = 'Earned ' + str(rando) + ' gold from the ' + str(session['building']) + ' ' + str(session['datetime'])
		session['activities'].insert(0, {'text':sentence, 'color':'green'})

	if request.form['building']=='cave':
		from time import gmtime, strftime
		rando = randint(5,10)
		session['score'] += rando
		session['building'] = request.form['building']
		session['datetime'] = strftime("%a, %d %b %Y %H:%M", gmtime())
		sentence = 'Earned ' + str(rando) + ' gold from the ' + str(session['building']) + ' ' + str(session['datetime'])
		session['activities'].insert(0, {'text':sentence, 'color':'green'})
	if request.form['building']=='house':
		from time import gmtime, strftime
		rando = randint(2,5)
		session['score'] += rando
		session['rando'] = rando
		session['building'] = request.form['building']
		session['datetime'] = strftime("%a, %d %b %Y %H:%M", gmtime())
		sentence = 'Earned ' + str(rando) + ' gold from the ' + str(session['building']) + ' ' + str(session['datetime'])
		session['activities'].insert(0, {'text':sentence, 'color':'green'})
	if request.form['building']=='casino':
		from time import gmtime, strftime
		rando = randint(-50,50)
		session['score'] += rando
		session['rando'] = rando
		session['building'] = request.form['building']
		session['datetime'] = strftime("%a, %d %b %Y %H:%M", gmtime())
		if rando > 0:
			sentence = 'Earned ' + str(rando) + ' gold from the ' + str(session['building']) + ' ' + str(session['datetime'])
			session['activities'].insert(0, {'text':sentence, 'color':'green'})
		if rando <= 0: 
			sentence = 'Lost' + str(rando) + ' gold from the ' + str(session['building']) + ' ....ouch ' + str(session['datetime'])
			session['activities'].insert(0, {'text':sentence, 'color':'red'})
	print session['activities']
	return redirect('/')

app.run(debug=True)


