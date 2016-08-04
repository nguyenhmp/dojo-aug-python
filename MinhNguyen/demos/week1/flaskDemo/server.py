from flask import Flask, render_template, request
app = Flask("the_boss")

@app.route('/')
def index():
	print dir(request)
	print request.user_agent
	return "hello world"

@app.route('/search')
def search():
	return "hello search"
def random():
	print "hello"
app.run(debug=True)