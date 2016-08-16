from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key ="keytomyheart"
import datetime

mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():

    query = "SELECT id, first_name, last_name, email, created_at FROM fullfriends"

    display = mysql.query_db(query)

    print "*"*10
    print display 
	
    return render_template('index.html', display=display)

@app.route('/friends', methods=['POST'])
def create():

    query = "INSERT INTO fullfriends(first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data= {'first_name' :request.form['first_name'], 'last_name' :request.form['last_name'], 'email' :request.form['email']}
    create_user = mysql.query_db(query, data)

    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit():

    query = "SELECT id, first_name, last_name, email, created_at FROM fullfriends"
    display = mysql.query_db(query)
    user_id = request.form['id'] #LOOK UP URL PARAMETERS
    print user_id 
    print *

    return render_template('show.html', display=display)

app.run(debug=True)