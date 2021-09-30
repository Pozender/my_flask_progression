from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello world in Flask</h1>"

@app.route("/try")
def trypage():
    return "<p>Bravo! Tu es le/la bienveunu sur cette page de teste</p>"

@app.route("/template/")
def templatepage():
    return render_template('index.html', name = 'Gérard')
@app.route("/form/")
def form():
    return render_template('form.html')