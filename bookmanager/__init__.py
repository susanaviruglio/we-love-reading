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
from bookmanager import routes