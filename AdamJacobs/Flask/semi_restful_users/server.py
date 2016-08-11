from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'sexyorange'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'users')

@app.route('/users')
def index():
  users = mysql.query_db("SELECT id, first_name, last_name, email, created_at FROM users")
  return render_template('index.html', users=users)

@app.route('/users/<id>')
def show(id):
  query = "SELECT id, first_name, last_name, email, created_at FROM users WHERE id = :id"
  data = {
    'id':id
  }
  users = mysql.query_db(query, data)
  return render_template('user.html', users=users)

@app.route('/users/new')
def new():
  return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
  query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email']
  }
  mysql.query_db(query, data)
  return redirect('/users/new')

@app.route('/users/<id>/edit')
def edit(id):
  return render_template('edit.html', id=id)

@app.route('/users/<id>', methods=['POST'])
def update(id):
  query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': id
  }
  mysql.query_db(query, data)
  return redirect('/users')

@app.route('/users/<id>/destroy')
def destroy(id):
  query = "DELETE FROM users WHERE id = :id"
  data = {
    'id': id
  }
  mysql.query_db(query, data)
  return redirect('/users')

app.run(debug=True)
