"""This will make sure to initialize the librarymanager application as a package, allowing to use
the own imports, as well as any standard imports."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa "No Quality Assurance"


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


# I have created an instance of the imported SQLAlchemy() class, which would be
# assigned to a variable of 'db'.
db = SQLAlchemy(app)

from librarymanager import routes # noqa 