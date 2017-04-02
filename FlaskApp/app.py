from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo
import bcrypt

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
	return render_template('index.html')

@app.route("/sign_in", methods=['POST'])
def sign_in():
    users = mongo.db.users
    login_user = user.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].enconde('utf-8')) == ogin_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

	return 'Invalid username/password combination'

@app.route("/view_pets")
def view_pets():
    return render_template('view_pets.html')

if __name__ == "__main__":
    app.run()
