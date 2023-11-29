# It will store all the data we need for our bookstore.
from librarymanager import db 

    
class Users(db.Model):
    # schema for Users model
    id_email = db.Column(db.String, unique=True, primary_key=True)
    password = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
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
    book_id = db.Column(db.String, db.ForeignKey("book.id_book", ondelete="CASCADE"))
    review_text = db.Column(db.Text)
    users_review = db.Column(db.String, db.ForeignKey("users.id_email", ondelete="CASCADE"))
    

    def __rep__(self):
        # to represent ISBN in the form of a string
        return "#{0} - ISBN: {1} | Users: {4}".format(
            self.id , self.book_id, self.users_review
        )


class Book(db.Model):
    # schema for Books model
    id_book = db.Column(db.String, unique=True, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String, nullable=False)
    book_reviews = db.relationship("Review", backref="book", cascade="all, delete", lazy=True)
    
    
    def __rep__(self):
        # __rep__ to represent itself in the form of a string
        return "# ID: {0} - Title: {1} - Author: {2} | ISBN: {5}".format(
            self.id_book, self.title, self.author, self.isbn
        )

# Creating database for my Book table
# Harry Potter Books
harry_potter_one = Book(
    id_book = "9788869183157",
    title = "Harry Potter and the Philosopher’s Stone",
    author = "J.K.Rowling",
    year = "1997-07-26",
    genre = "Fantasy"
)


harry_potter_two = Book(
    id_book = "9788869185182",
    title = "Harry Potter and the Chamber of Secrets",
    author = "J.K.Rowling",
    year = "2002-11-03",
    genre = "Fantasy"
)

harry_potter_three = Book(
    id_book = "9788869186127",
    title = "Harry Potter and the Prisioner of Azkaban",
    author = "J.K.Rowling",
    year = "2004-05-31",
    genre = "Fantasy"
)

harry_potter_four = Book(
    id_book = "9780439139595",
    title = "Harry Potter and the Goblet of Fire ",
    author = "J.K.Rowling",
    year = "2005-11-08",
    genre = "Fantasy"
)

harry_potter_five = Book(
    id_book = "9780439358064",
    title = "Harry Potter and the Order of the Phoenix ",
    author = "J.K.Rowling",
    year = "2007-07-12",
    genre = "Fantasy"
)

harry_potter_six = Book(
    id_book = "9780439791328",
    title = "Harry Potter and the Half-Blood Prince",
    author = "J.K.Rowling",
    year = "2009-07-15",
    genre = "Fantasy"
)

harry_potter_seven = Book(
    id_book = "9780545010221",
    title = "Harry Potter and the Deathly Hallows ",
    author = "J.K.Rowling",
    year = "2007-07-21",
    genre = "Fantasy"
)

#db.session.add(harry_potter_one)
#db.session.add(harry_potter_two)
#db.session.add(harry_potter_three)
#db.session.add(harry_potter_four)
#db.session.add(harry_potter_five)
#db.session.add(harry_potter_six)
#db.session.add(harry_potter_seven)

after_one = Book(
    id_book = "9783453491168",
    title = "After",
    author = "Anna Todd",
    year = "2014-10-21",
    genre = "Romance"
)

after_two = Book(
    id_book = "9781501104008",
    title = "After We Collided",
    author = "Anna Todd",
    year = "2020-09-02",
    genre = "Romance"
)

after_three = Book(
    id_book = "9788408135678",
    title = "After We Fell",
    author = "Anna Todd",
    year = "2021-09-30",
    genre = "Romance"
)

after_four = Book(
    id_book = "9781501106408",
    title = "After Ever Happy",
    author = "Anna Todd",
    year = "2022-09-07",
    genre = "Romance"
)

#db.session.add(after_one)
#db.session.add(after_two)
#db.session.add(after_three)
#db.session.add(after_four)

lord_of_rings_one = Book (
    id_book="9780007136599",
    title="The Lord of the Rings: The Fellowship of the Ring",
    author="J. R. R. Tolkien",
    year="1954-07-29",
    genre="Fantasy"
)

lord_of_rings_two = Book (
    id_book="9788445071762",
    title="The Lord of the Rings: The Fellowship of the Ring",
    author="J. R. R. Tolkien",
    year="1954-11-11",
    genre="Fantasy"
)

lord_of_rings_three = Book (
    id_book="9788845255427",
    title="The Lord of the Rings: The Return of the King",
    author="J. R. R. Tolkien",
    year="1955-10-20",
    genre="Fantasy"
)

db.session.add(lord_of_rings_one)
db.session.add(lord_of_rings_two)
db.session.add(lord_of_rings_three)
db.session.commit()

