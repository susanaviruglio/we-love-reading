"""Routes where I have include Flask functionality and imported render_template,
from bookmanager, I have imported app and db. To get the app running I have created 
a basic app route to start with which it will be my home page.
I also had to import flash, session and password security to create the user login"""
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
    """I created this variable to create a list where I can query all the data from the Book
     database, I have added Review table as well because it will appear all the users reviews in
     each book once submited """
    books = list(Book.query.order_by(Book.id_book, Book.title, Book.author, Book.year,
    Book.genre, Book.image, Book.introduction).all())
    reviews = list(Review.query.order_by(Review.book_id, Review.review_text,
    Review.users_review).all())
    return render_template("books.html", books = books, reviews=reviews)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ Register section for the user to create their own user account, if the user request to Post,
    then the user would need to fill the form and click submit"""
    if request.method == "POST":
        id_email = request.form.get("id_email")
        password = request.form.get("password")
        fname = request.form.get("fname")
        lname = request.form.get("lname")

        # Hash the password before storing it to the database so the password is save.
        password_hash = generate_password_hash(password)

        # Check if the user with the given email already exists, 
        #  if it exists it will print a message
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
        # Once the account it is create it will get redirected to this site.
        return redirect(url_for("profile"))

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    """Login to the users account from the database, if the user request Post, they will need
    to add email and password from the database"""

    if request.method == "POST":
        email = request.form.get("id_email")
        password = request.form.get("password")

        user = Users.query.filter_by(id_email=email).first()
        # if the user does not exists it will print this message
        if not user:
            flash('Invalid email address. Please try again.', 'error')
            return redirect(url_for("signin"))
        # if the password is incorrect then it will get this message
        if not check_password_hash(user.password, password):
            flash('Invalid password. Please try again.', 'error')
            return redirect(url_for("signin"))

        # Successful login is equal to True, user_id = user.id_email
       
        session['logged_in'] = True
        session['user_id'] = user.id_email
        # once log in it will get to the profile site.
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
    """ the user will only see the profile once it is login, if it is not login then profile
    will be hidden"""
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
