from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'illuminatikey'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def student_feedback():
	session['name'] = request.form['name']
	if len(session['name']) < 1:
		flash("Please enter your full name.")
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	if len(session['comment']) < 1:
		flash("Please enter a comment.")
	elif len(session['comment']) > 120:
		flash("Your comment cannot be more than 120 characters.")
	print len(session['comment'])
	return render_template("result.html")

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)