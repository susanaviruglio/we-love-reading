
"""
The entire application needs to be its own Python package.
This file initializes the bookmanager application as a package.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import environment variables if env.py exists
if os.path.exists("env.py"):
    import env  # noqa: F401

# Create the Flask application
app = Flask(__name__)

# Local development configuration
app.config["SECRET_KEY"] = "local-development-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///we_love_reading.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after creating app and db
from bookmanager import routes
