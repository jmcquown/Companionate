from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/sign_in")
def sign_in():
	return render_template('sign_in.html')

@app.route("/view_pets")
def view_pets():
    return render_template('view_pets.html')

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

if __name__ == "__main__":
    app.run()
