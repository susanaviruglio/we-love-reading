#I have to import os , in order to utilize environment variables within this file and
# import app variable which I created within librarymanager.
import os
from bookmanager import app 


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP"),
        port = os.environ.get("PORT"),
        debug = os.environ.get("DEBUG")
)
