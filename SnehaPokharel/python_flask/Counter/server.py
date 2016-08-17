from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'snebaybay'

@app.route('/')
def counter():
    try:
        request.session['counter']
    except:
        request.session['counter'] = 0
    
    session['counter'] += 1
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    print 'NINJASSS'
    session['counter'] += 1
    return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)