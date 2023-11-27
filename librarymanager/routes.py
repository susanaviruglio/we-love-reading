from flask import render_template, request, redirect, url_for
from librarymanager import app, db
from librarymanager.models import Book, Users, Review

@app.route("/")
def home():
    return render_template("index.html")
    # if I change the name it will become the homepage.



@app.route("/books", methods=["GET", "POST"])
def books():
    return render_template("books.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    
    if request.method == "POST":
        users = Users(
            id_email = request.form.get("id_email"),
            password = request.form.get("password"),
            fname = request.form.get("fname"),
            lname = request.form.get("lname") 
        )
        db.session.add(users)
        db.session.commit()
        return redirect(url_for("profile"))
    return render_template("signup.html")


@app.route("/signin", methods=["GET"])
def signin():
    if request.method == "GET":
        users = Users(
            id_email = request.form.get("id_email"),
            password = request.form.get("password"),
        )
        db.session.add(users)
        db.session.commit()
        return redirect(url_for("profile"))
    return render_template("signin.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    
    return render_template("profile.html")


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """When the user clicks 'Add Review' button in the profile page, this will use the'GET'
       method and render the 'add_review' template. Once they submit the form, this
       will call the same function, but will check if the request being made is a “POST“ method,
       which posts data somewhere, such as a database. """
    if request.method == "POST":
        # add a review to the database.
        # if I use request method I have to import it to flask as well on the top.
        review = Review(
            book_id=request.form.get("book_id"),
            review_text=request.form.get("review_text"),
            users_review=request.form.get("users_review")
            )
        db.session.add(review)
        db.session.commit()
        # after the form gets submitted, and I have added and committed 
        # the new data to our database, I can redirect the user to the 'profile' page.
        return redirect(url_for("books"))
    return render_template("add_review.html")
