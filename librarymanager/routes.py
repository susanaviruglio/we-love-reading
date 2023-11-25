from flask import render_template
from librarymanager import app, db
from librarymanager.models import Book, Users, Review

@app.route("/")
def home():
    return render_template("signup.html")
    # if I change the name it will become the homepage.