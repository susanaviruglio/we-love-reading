# It will store all the data we need for our bookstore.
from librarymanager import db 

 
class Book(db.Model):
    # schema for Books model
    id_book = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String)
    book_reviews = db.relationship("Review", backref="book", cascade="all, delete", lazy=True)
    
    
    def __rep__(self):
        # __rep__ to represent itself in the form of a string
        return "# ID: {0} - Title: {1} - Author: {2} | ISBN: {5}".format(
            self.id_book, self.title, self.author, self.isbn
        )
    
    
class Users(db.Model):
    # schema for Users model
    id_email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    fname = db.Column(db.String)
    lname = db.Column(db.String, nullable=False)
    about_me = db.Column(db.Text, nullable=False)
    favourite_book = db.Column(db.String)
    reviews = db.relationship("Review", backref="users", cascade="all,delete", lazy=True)
    
    
    def __rep__(self):
        # to represent the user details in the form of a string
        return "# Email: {0} - Name: {2} - Last Name: {3}".format(
            self.id_email, self.fname, self.lname
        )
    

class Review(db.Model):
    # schema for Reviews model
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String, db.ForeignKey("book.id_book", ondelete="CASCADE"),
    nullable=False)
    review_text = db.Column(db.Text)
    users_review = db.Column(db.String, db.ForeignKey("users.id_email", ondelete="CASCADE"),nullable=False)
    

    def __rep__(self):
        # to represent ISBN in the form of a string
        return "#{0} - ISBN: {1} | Users: {4}".format(
            self.id , self.book_id, self.users_review
        )
