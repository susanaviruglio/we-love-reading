""" I have created the main python file which it will run the entire application where
I have to import os , in order to utilize environment variables within this file and
 import app variable which I created within bookmanager, which it has been defined
 within the __init__ file"""
import os
from bookmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("DEBUG", "false").lower() == "true",
    )