"""
The entire application needs to be its own Python package.
This file initializes the bookmanager application as a package.
"""

import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import environment variables if env.py exists
if os.path.exists("env.py"):
    import env  # noqa: F401

# Create the Flask application
app = Flask(__name__)

# Production-ready config with environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")

database_url = os.environ.get("DATABASE_URL", "sqlite:///we_love_reading.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after creating app and db
from bookmanager import routes  # noqa: E402
from bookmanager.models import (  # noqa: E402
    Book,
    harry_potter_one, harry_potter_two, harry_potter_three,
    harry_potter_four, harry_potter_five, harry_potter_six,
    harry_potter_seven,
    after_one, after_two, after_three, after_four,
    lord_of_rings_one, lord_of_rings_two, lord_of_rings_three,
)

with app.app_context():
    db.create_all()

    if Book.query.first() is None:
        books = [
            harry_potter_one, harry_potter_two, harry_potter_three,
            harry_potter_four, harry_potter_five, harry_potter_six,
            harry_potter_seven,
            after_one, after_two, after_three, after_four,
            lord_of_rings_one, lord_of_rings_two, lord_of_rings_three,
        ]

        for book in books:
            book.year = datetime.strptime(book.year, "%Y-%m-%d").date()

        db.session.add_all(books)
        db.session.commit()

    # Update the saved image URL for Harry Potter 1
    book = Book.query.filter_by(id_book="9788869183157").first()
    if book:
        book.image = (
            "https://upload.wikimedia.org/wikipedia/en/6/6b/"
            "Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg"
        )
        db.session.commit()
    else:
        app.logger.warning("Harry Potter 1 no está en la base de datos.")