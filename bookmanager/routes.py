from flask import render_template, request, redirect, url_for, flash, session
from bookmanager import app, db
from bookmanager.models import Book, Users, Review
from werkzeug.security import generate_password_hash, check_password_hash



@app.route("/")
def home():
    return render_template("index.html")
    # if I change the name it will become the homepage.


@app.route("/books")
def books():
    books = list(Book.query.order_by(Book.id_book, Book.title, Book.author, Book.year,
    Book.genre, Book.image, Book.introduction).all())
    reviews = list(Review.query.order_by(Review.book_id, Review.review_text,
    Review.users_review).all())
    return render_template("books.html", books=books, reviews=reviews)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        id_email = request.form.get("id_email")
        password = request.form.get("password")
        fname = request.form.get("fname")
        lname = request.form.get("lname")

        # Hash the password before storing it
        password_hash = generate_password_hash(password)

        # Check if the user with the given email already exists
        existing_user = Users.query.filter_by(id_email=id_email).first()

        if existing_user:
            flash('Email already in use. Please choose a different email.', 'error')
            return redirect(url_for("signup"))

        # Create a new Users instance with hashed password
        user = Users(
            id_email=id_email,
            password=password_hash,
            fname=fname,
            lname=lname
        )

        # Add the user to the database
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("profile"))

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":
        email = request.form.get("id_email")
        password = request.form.get("password")

        user = Users.query.filter_by(id_email=email).first()

        if not user:
            flash('Invalid email address. Please try again.', 'error')
            return redirect(url_for("signin"))

        if not check_password_hash(user.password, password):
            flash('Invalid password. Please try again.', 'error')
            return redirect(url_for("signin"))

        # Successful login
        print("Login successful")
        session['logged_in'] = True
        session['user_id'] = user.id_email

        return redirect(url_for('profile'))

    return render_template("signin.html")


@app.route('/logout')
def logout():
    """
    Function to clear all session data to log out the user,
    and redirect them to home page
    """
    session.clear()  # Clear all session data
    return redirect(url_for('home'))


@app.route("/profile", methods=["GET", "POST"])
def profile():
       # Check if the user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('signin'))  # Redirect to the login page if not logged in

        # Fetch the user data from the database
    user_id = session.get('user_id')
    user = Users.query.filter_by(id_email=user_id).first()

    return render_template("profile.html", user=user)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """When the user clicks 'Add Review' button in the profile page, this will use the'GET'
       method and render the 'add_review' template. Once they submit the form, this
       will call the same function, but will check if the request being made is a “POST“ method,
       which posts data somewhere, such as a database. """
    books = list(Book.query.order_by(Book.id_book, Book.title, Book.author, Book.year,
    Book.genre, Book.image, Book.introduction).all())
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
        return redirect(url_for("add_review"))
    return render_template("add_review.html", books=books)
