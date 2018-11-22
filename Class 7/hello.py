from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////users.db'
db.init_app(app)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
