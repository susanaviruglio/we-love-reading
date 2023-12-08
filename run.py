""" I have created the main python file which it will run the entire application where
I have to import os , in order to utilize environment variables within this file and
 import app variable which I created within bookmanager, which it has been defined
 within the __init__ file"""
import os
from bookmanager import app 


if __name__ == "__main__":
    """ I need to tell the aplication where and how to run the application,
    checking that the name class is equal to main, if it match then I will get 
    the app running."""
    app.run(
        # each of these are stored in the environment variable
        host = os.environ.get("IP"), 
        port = os.environ.get("PORT"),
        debug = os.environ.get("DEBUG")
)
