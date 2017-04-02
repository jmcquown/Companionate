from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'hack-princeton'
app.config['MONGO_URL'] = 'mongodb://hack:princeton@ds149040.mlab.com:49040/hack-princeton'

mongo = PyMongo(app)

@app.route("/")
def index():
    # if 'username' in session:
        # return "fuck"
        # return 'You are logged in as ' + session['username']
	return render_template('index.html')

@app.route("/sign_in")
def sign_in():
    return render_template('sign_in.html')

@app.route("/login", methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].enconde('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route("/view_pets")
def view_pets():
    return render_template('view_pets.html')

if __name__ == "__main__":
    app.run()
