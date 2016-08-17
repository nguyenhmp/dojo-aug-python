from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from re import match, search

app = Flask(__name__)
app.secret_key = 'tributetothegreatestkeyintheworld'
mysql = MySQLConnector(app, 'the_wall')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
	# Clear session to remove id
	if 'id' in session:
		session.clear()
	return render_template('index.html')

@app.route('/wall')
def signIn():
	messageQuery = "SELECT messages.id as message_id, messages.message, messages.created_at as message_time, users.id as user_id, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY message_id DESC"
	wall_data = mysql.query_db(messageQuery)
	commentQuery = "SELECT comments.id as comment_id, comments.comment, comments.created_at as comment_time, comments.message_id, comments.user_id, users.first_name, users.last_name FROM comments JOIN users ON users.id = comments.user_id ORDER BY comment_id"
	comment_data = mysql.query_db(commentQuery)
	return render_template('content.html', wall_data=wall_data, comment_data=comment_data)

# FUTURE FEATURE: user page with message statistics
# @app.route('/user/<user_id>')
# def userdata(user_id):
# 	return render_template('user.html', user_data=user_data)

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	query = "SELECT id, first_name, email, pw_hash FROM users WHERE email=:email LIMIT 1"
	data = { 'email': email }
	user = mysql.query_db(query, data)
	if user:
		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
			session['id'] = user[0]['id']
			session['first_name'] = user[0]['first_name']
			return redirect('/wall')
		else:
			flash("Invalid Password")
	else:
		flash("Email not found")
	return redirect('/')


@app.route('/register', methods=['POST'])
def register():
	errorCheck = False
	# Validate First Name
	first_name = request.form['first_name']
	if len(first_name) < 2:
		flash("First Name must be at least 2 characters long")
		errorCheck = True
	elif match(r'[^a-zA-Z]', str(first_name)):
		flash("First Name must only contain letters")
		errorCheck = True
	# Validate Last Name
	last_name = request.form['last_name']
	if len(last_name) < 2:
		flash("Last Name must be at least 2 characters long")
		errorCheck = True
	elif search(r'[^a-zA-Z]', str(last_name)):
		flash("Last Name must only contain letters")
		errorCheck = True
	# Validate Email
	email = request.form['email']
	query = "SELECT email FROM users WHERE email = :email"
	data = { 'email': email }
	emailCheck = mysql.query_db(query, data)
	if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
		flash("Please enter a valid email")
		errorCheck = True
	elif emailCheck:
		flash("Email already in use")
		errorCheck = True
	# Validate Password
	password = request.form['password']
	if len(password) < 8:
		flash("Password must be at least 8 characters long")
		errorCheck = True
	# Validate Conf_Password
	conf_password = request.form['conf_password']
	if password != conf_password:
		flash("Password does not match")
		errorCheck = True
	# Check if all validation checks passed
	if errorCheck == True:
		return redirect('/')
	else:
		pw_hash = bcrypt.generate_password_hash(password)
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
		data = {
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
				'pw_hash': pw_hash
				}
		session['id'] = mysql.query_db(query, data)
		flash("You have successfully registered!")
		return redirect('/wall')

@app.route('/addmessage/<user_id>', methods=['POST'])
def postmessage(user_id):
	message = request.form['message']
	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
	data = { 'user_id': user_id, 'message': message }
	mysql.query_db(query, data)
	flash("Successfully posted new message!")
	return redirect('/wall')

@app.route('/deletemessage/<message_id>', methods=['POST'])
def removeMessage(message_id):
	# Remove dependent comments
	query = "DELETE FROM comments WHERE message_id = :message_id"
	data = { 'message_id': message_id }
	mysql.query_db(query, data)
	# Remove message
	query = "DELETE FROM messages WHERE id = :message_id"
	data = { 'message_id': message_id }
	mysql.query_db(query, data)
	flash("Message successfully removed")
	return redirect('/wall')

@app.route('/addcomment/<message_id>/<user_id>', methods=['POST'])
def postComment(message_id, user_id):
	comment = request.form['comment']
	query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
	data = {
			'message_id': message_id,
			'user_id': user_id,
			'comment': comment,
			}
	mysql.query_db(query, data)
	flash("Successfully posted new comment!")
	return redirect('/wall')

@app.route('/deletecomment/<comment_id>', methods=['POST'])
def removeComment(comment_id):
	query = "DELETE FROM comments WHERE id = :comment_id"
	data = { 'comment_id': comment_id }
	mysql.query_db(query, data)
	flash("Comment successfully deleted")
	return redirect('/wall')

app.run(debug=True)