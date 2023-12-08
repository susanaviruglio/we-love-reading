""" The entire application need to be its own Python package so I created bookmanager folder.
    This file will make sure to initialize the bookmanager 
    application as a package, allowing to use
    the own imports, as well as any standard imports."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    # in order to use the env.py file I need to import it
    import env  # noqa "No Quality Assurance"


# next, I have created an instance of the imported Flask() class, it would be stored
# in a variable called app which takes the default name Flask__name__module.
app = Flask(__name__)
# two variables from the environment variables, it will also support to upload it to Heroku
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

# I have created an instance of the imported SQLAlchemy() class, 
#which would be assigned to a variable of 'db'.
db = SQLAlchemy(app)
# from the bookmanager package I need to import routes, the reason is imported last,
# it is because the routes will rely on using app and db respectively 
# if I try to do it before I will get get circular errors.
from bookmanager import routes  