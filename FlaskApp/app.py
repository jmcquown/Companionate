from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo
import bcrypt

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def main():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
	return render_template('index.html')

@app.route("/sign_in")
def sign_in():
	return render_template('sign_in.html')

@app.route("/view_pets")
def view_pets():
    return render_template('view_pets.html')

if __name__ == "__main__":
    app.run()
