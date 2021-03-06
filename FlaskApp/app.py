from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
from flask import Markup
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'hack-princeton'
app.config['MONGO_URI'] = 'mongodb://hack:princeton@ds149040.mlab.com:49040/hack-princeton'

mongo = PyMongo(app)

app.secret_key="shhhhhhhhhhhitsasecr3t"

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
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return render_template('view_pets.html')
    flash(Markup("Invalid username/password"))
    return redirect(url_for('sign_in'))

@app.route("/view_pets")
def view_pets():
    return render_template('view_pets.html')

@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['InputEmail']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['InputPassword'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['InputEmail'], 'password' : hashpass, 'street' : request.form['InputStreetAddress'], 'city' : request.form['InputCityAddress'], 'zip' : request.form['InputZipcode'], 'phone' : request.form['InputPhone']})
            session['username'] = request.form['InputEmail']
            return redirect(url_for('index'))
        return "Username already exists!"    

    return render_template('sign_up.html')

if __name__ == "__main__":
    app.run()
