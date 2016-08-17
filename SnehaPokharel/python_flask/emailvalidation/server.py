from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'heyhey'

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app,'emailvalidation')

@app.route('/')
def index():
    email = mysql.query_db("SELECT * FROM email")
    print email
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def email():
    type(request.form['email_id'])
    session['result'] = request.form['email_id']
    
    if EMAIL_REGEX.match(request.form['email_id']):
        query = "INSERT INTO email (email_add, created_on, updated_on) VALUES( :email_add, NOW(), NOW())"
        data = {'email_add' :request.form['email_id']}
        mysql.query_db(query, data)
        pass 
    elif request.form['email_id'] == "":
        pass 
    else:
        flash("Please enter a valid email address.") 
    print request.form['email_id']
    return redirect('/')

@app.route('/success')
def showsuccess():
    query = "SELECT * FROM email"                           # define your query
    email = mysql.query_db(query)
    

    # if request.form['delete']: #attempt to delete data ---> FAILED. 
    #     query = "DELETE FROM email WHERE id = :id"
    #     data = {'id': email_id}
    #     mysql.query_db(query, data)
                                                                # run query with query_db()
    return render_template('success.html', all_email=email)

app.run(debug=True)