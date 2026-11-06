# It will store all the data we need for our bookstore.
from bookmanager import app, db



class Review(db.Model):
    # schema for Reviews model
    id = db.Column(db.Integer, primary_key=True) # the id is an integer
    book_id = db.Column(db.String, db.ForeignKey("book.id_book", ondelete="CASCADE")) # connected to the book ISBN
    review_text = db.Column(db.Text) # review information
    users_review = db.Column(db.String, db.ForeignKey("users.id_email", ondelete="CASCADE")) # user who posts the review
    
    def __repr__(self):
        # to represent ISBN in the form of a string
        return "#{0} - ISBN: {1} | Users: {4}".format(
            self.id , self.book_id, self.users_review
        )


class Users(db.Model):
    # schema for Users model
    id_email = db.Column(db.String, unique=True, primary_key=True) # the id is a string which is the users' email
    password = db.Column(db.String, nullable=False) # the password which it has been hashed in routes
    fname = db.Column(db.String, nullable=False) # user first name
    lname = db.Column(db.String, nullable=False) # user last name
    reviews = db.relationship("Review", backref="users", cascade="all,delete", lazy=True) # review published
    
    
    def __repr__(self):
        # to represent the user details in the form of a string
        return "# Email: {0} - Name: {2} - Last Name: {3}".format(
            self.id_email, self.fname, self.lname
        )


# I have created this user to test my user table in the database
first_user = Users(
    id_email = "hermione@gmail.com",
    password = "witch",
    fname = "Hermione",
    lname = "Granger"
)
# I have added manually and then commented
# db.session.add(first_user)


class Book(db.Model):
    # schema for Books model
    id_book = db.Column(db.String, unique=True, primary_key=True) # book id is the unique ISBN 
    title = db.Column(db.String, unique=True, nullable=False) # book title unique
    author = db.Column(db.String, nullable=False) # book author
    year = db.Column(db.Date, nullable=False) # book author
    genre = db.Column(db.String, nullable=False) # book genre
    book_reviews = db.relationship("Review", backref="book", cascade="all, delete", lazy=True) # reviews related to each book
    image = db.Column(db.String) # image source from each book (link)
    introduction = db.Column(db.String) # book introduction
    
    def __repr__(self):
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
    genre = "Fantasy",
    introduction = "Harry Potter thinks he is an ordinary boy - until he is rescued by an owl, taken to Hogwarts School of Witchcraft and Wizardry, learns to play Quidditch and does battle in a deadly duel. The Reason ... HARRY POTTER IS A WIZARD! Find out some reviews!!",
    image = "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg"
)


harry_potter_two = Book(
    id_book = "9788869185182",
    title = "Harry Potter and the Chamber of Secrets",
    author = "J.K.Rowling",
    year = "2002-11-03",
    genre = "Fantasy",
    introduction = "Ever since Harry Potter had come home for the summer, the Dursleys had been so mean and hideous that all Harry wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he’s packing his bags, Harry receives a warning from a strange impish creature who says that if Harry returns to Hogwarts, disaster will strike.",
    image = "https://upload.wikimedia.org/wikipedia/en/5/5c/Harry_Potter_and_the_Chamber_of_Secrets.jpg"
)

harry_potter_three = Book(
    id_book = "9788869186127",
    title = "Harry Potter and the Prisioner of Azkaban",
    author = "J.K.Rowling",
    year = "2004-05-31",
    genre = "Fantasy",
    introduction = "Harry Potter, along with his best friends, Ron and Hermione, is about to start his third year at Hogwarts School of Witchcraft and Wizardry. Harry can't wait to get back to school after the summer holidays. (Who wouldn't if they lived with the horrible Dursleys?) But when Harry gets to Hogwarts, the atmosphere is tense. There's an escaped mass murderer on the loose, and the sinister prison guards of Azkaban have been called in to guard the school...",
    image = "https://upload.wikimedia.org/wikipedia/en/a/a0/Harry_Potter_and_the_Prisoner_of_Azkaban.jpg"
)

harry_potter_four = Book(
    id_book = "9780439139595",
    title = "Harry Potter and the Goblet of Fire ",
    author = "J.K.Rowling",
    year = "2005-11-08",
    genre = "Fantasy",
    introduction = "It is the summer holidays and soon Harry Potter will be starting his fourth year at Hogwarts School of Witchcraft and Wizardry. Harry is counting the days: there are new spells to be learnt, more Quidditch to be played, and Hogwarts castle to continue exploring. But Harry needs to be careful - there are unexpected dangers lurking...",
    image = "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Harry_Potter_and_the_Goblet_of_Fire_cover.png/220px-Harry_Potter_and_the_Goblet_of_Fire_cover.png"
)

harry_potter_five = Book(
    id_book = "9780439358064",
    title = "Harry Potter and the Order of the Phoenix ",
    author = "J.K.Rowling",
    year = "2007-07-12",
    genre = "Fantasy",
    introduction = "Harry Potter is about to start his fifth year at Hogwarts School of Witchcraft and Wizardry. Unlike most schoolboys, Harry never enjoys his summer holidays, but this summer is even worse than usual. The Dursleys, of course, are making his life a misery, but even his best friends, Ron and Hermione, seem to be neglecting him.",
    image = "https://upload.wikimedia.org/wikipedia/en/7/70/Harry_Potter_and_the_Order_of_the_Phoenix.jpg"
)

harry_potter_six = Book(
    id_book = "9780439791328",
    title = "Harry Potter and the Half-Blood Prince",
    author = "J.K.Rowling",
    year = "2009-07-15",
    genre = "Fantasy",
    introduction = "It is the middle of the summer, but there is an unseasonal mist pressing against the windowpanes. Harry Potter is waiting nervously in his bedroom at the Dursleys' house in Privet Drive for a visit from Professor Dumbledore himself. One of the last times he saw the Headmaster, he was in a fierce one-to-one duel with Lord Voldemort, and Harry can't quite believe that Professor Dumbledore will actually appear at the Dursleys' of all places. Why is the Professor coming to visit him now?",
    image = "https://upload.wikimedia.org/wikipedia/en/b/b5/Harry_Potter_and_the_Half-Blood_Prince_cover.png"
)

harry_potter_seven = Book(
    id_book = "9780545010221",
    title = "Harry Potter and the Deathly Hallows ",
    author = "J.K.Rowling",
    year = "2007-07-21",
    genre = "Fantasy",
    introduction = "Harry has been burdened with a dark, dangerous and seemingly impossible task: that of locating and destroying Voldemort's remaining Horcruxes. Never has Harry felt so alone, or faced a future so full of shadows. But Harry must somehow find within himself the strength to complete the task he has been given. He must leave the warmth, safety and companionship of The Burrow and follow without fear or hesitation the inexorable path laid out for him...",
    image = "https://upload.wikimedia.org/wikipedia/en/a/a9/Harry_Potter_and_the_Deathly_Hallows.jpg"
)

after_one = Book(
    id_book = "9783453491168",
    title = "After",
    author = "Anna Todd",
    year = "2014-10-21",
    genre = "Romance",
    introduction = "Tessa is a good girl with a sweet, reliable boyfriend back home. She’s got direction, ambition, and a mother who’s intent on keeping her that way. But she’s barely moved into her freshman dorm when she runs into Hardin. With his tousled brown hair, cocky British accent, tattoos, and lip ring, Hardin is cute and different from what she’s used to",
    image = "https://upload.wikimedia.org/wikipedia/en/e/e8/After_2014_novel_cover.jpg"
)

after_two = Book(
    id_book = "9781501104008",
    title = "After We Collided",
    author = "Anna Todd",
    year = "2020-09-02",
    genre = "Romance",
    introduction = "After a tumultuous beginning to their relationship, Tessa and Hardin were on the path to making things work. Tessa knew Hardin could be cruel, but when a bombshell revelation is dropped about the origins of their relationship—and Hardin’s mysterious past—Tessa is beside herself.",
    image = "https://upload.wikimedia.org/wikipedia/en/4/41/After_We_Collided_novel_cover.jpeg"
)

after_three = Book(
    id_book = "9788408135678",
    title = "After We Fell",
    author = "Anna Todd",
    year = "2021-09-30",
    genre = "Romance",
    introduction = "Tessa knows Hardin loves her and will do anything to protect her, but there’s a difference between loving someone and being able to have them in your life. This cycle of jealousy, unpredictable anger, and forgiveness is exhausting.",
    image = "https://m.media-amazon.com/images/I/710zHnmzYlS._SL1500_.jpg"
)

after_four = Book(
    id_book = "9781501106408",
    title = "After Ever Happy",
    author = "Anna Todd",
    year = "2022-09-07",
    genre = "Romance",
    introduction = "Book Four of the After series—now newly revised and expanded, Anna Todd’s After fanfiction racked up 1 billion reads online and captivated readers across the globe. Experience the Internet’s most talked-about book for yourself!",
    image = "https://m.media-amazon.com/images/I/71eeR6AxuJL._SL1500_.jpg"
)


lord_of_rings_one = Book (
    id_book="9780007136599",
    title="The Lord of the Rings: The Fellowship of the Ring",
    author="J. R. R. Tolkien",
    year="1954-07-29",
    genre="Fantasy",
    introduction = "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them.",
    image = "https://m.media-amazon.com/images/I/913sMwNHsBL._SL1500_.jpg"
)

lord_of_rings_two = Book (
    id_book="9788445071762",
    title="The Lord of the Rings: The Two Towers",
    author="J. R. R. Tolkien",
    year="1954-11-11",
    genre="Fantasy",
    introduction = " Having fled the Shire in their escape from Sauron's Dark Riders, Frodo and the Fellowship of the Ring have journeyed to Rivendell and beyond. Their mission is to reach the Mountain of Fire in Mordor, where the Ruling Ring can be destroyed.",
    image = "https://i.ebayimg.com/images/g/2WkAAOSwlZNjlfzY/s-l500.jpg"
)

lord_of_rings_three = Book (
    id_book="9788845255427",
    title="The Lord of the Rings: The Return of the King",
    author="J. R. R. Tolkien",
    year="1955-10-20",
    genre="Fantasy",
    introduction = "To defeat Sauron, the One Ring must be destroyed in the fires of Mount Doom. But the way is impossibly hard, and Frodo is weakening. The Ring corrupts all who bear it and Frodo's time is running out.",
    image = "https://i.ebayimg.com/images/g/1xAAAOSwtoFlUDRB/s-l500.jpg"
)

# I have added then manually and commented to avoid errors
#db.session.add(harry_potter_one)
#db.session.add(harry_potter_two)
#db.session.add(harry_potter_three)
#db.session.add(harry_potter_four)
#db.session.add(harry_potter_five)
#db.session.add(harry_potter_six)
#db.session.add(harry_potter_seven)

#db.session.add(after_one)
#db.session.add(after_two)
#db.session.add(after_three)
#db.session.add(after_four)

#db.session.add(lord_of_rings_one)
#db.session.add(lord_of_rings_two)
#db.session.add(lord_of_rings_three)
#db.session.commit()

