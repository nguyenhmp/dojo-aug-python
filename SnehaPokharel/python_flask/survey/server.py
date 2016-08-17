from flask import Flask, render_template, request, redirect, flash, session  
app = Flask(__name__)
app.secret_key = 'Mood'

@app.route('/')
def survey():
    return render_template('index.html')
@app.route('/submit', methods = ['POST'])
def results():
	data = request.form
	print data 

	if request.form['name'] == "":
		flash("You must put in your name!")
	else:
		pass 
	
	if request.form['description'] == "" :
		flash("You must put in a comment!")
	else:
		pass 

	if len(request.form['description']) > 120:
		flash("Comment is too long. Please reduce")	
	else:
		pass 

	return render_template('users.html', data=data)

app.run(debug=True)