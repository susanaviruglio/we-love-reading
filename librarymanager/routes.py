from flask import render_template
from librarymanager import app, db
from librarymanager.models import Book, Users, Review

@app.route("/")
def home():
    return render_template("base.html")
    # if I change the name it will become the homepage.


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")
