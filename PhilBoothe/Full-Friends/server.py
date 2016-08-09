from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'tributetothegreatestkeyintheworld'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', friend_list=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
			}
	mysql.query_db(query, data)
	flash("Welcome " + str(request.form['first_name']) + "! Congrats on becoming my newest Best Friend Forever!")
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id=:id"
	data = { 'id': id }
	friend = mysql.query_db(query, data)
	return render_template('edit.html', friend_list=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
	data = {
			'id': id,
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
			}
	mysql.query_db(query, data)
	flash("Successfully updated " + str(request.form['first_name'] + "'s info!"))
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = { 'id': id }
	mysql.query_db(query, data)
	flash("Successfully Initiated Forget Friend Function!")
	return redirect('/')

app.run(debug=True)