# We ❤️ Reading
## Backend Development Milestone Project by Susana Viruglio

Build a book review and recommendation site.

<img src= bookmanager/static/images/presentation.png>


### External User Goals

- Find books they would like to read and write reviews.

### Site Owner's Goals

- Get popularity by letting users to write the own reviews.

### Potential Features To Include

- Create a web application that allows users to upload details of books, including book name, author name, link to cover image and any other relevant fields. Allow users to write comments about any book.
- Create a web application that allows users to have their own profile area. 

## UX AIMS

- Users should easily find their way around the website.
-  Clear and intuitive navigation menus, categorized book sections, and a user-friendly layout.
- Ensure the website is accessible and functional across various devices and screen sizes.
- Present books in an engaging manner to capture user attention.
-  Enable users to share their opinions and experiences.


## USERS STORIES

1. **How can I write a review?** I would like to write a review about my favourite book.

2. **I want to discover new books based on genres or categories,** so I can find titles that match my interests.

3. **I want to create a personalized profile,** allowing me to write comments for the books I've read.

4. **I want a clear and intuitive homepage,** providing an overview of popular books, reviews, and site features.

5. **I want the website to be responsive and mobile-friendly,** enabling me to access and navigate it from my smartphone or tablet.


## DESIGN EVOLUTION

**First idea for desktop**

<img src= bookmanager/static/images/figma-desktop-design.jpg>

**First idea for phone**

<img src= bookmanager/static/images/figma-phone-design.jpg>

## DATA BASE EVOLUTION

**ERDplus Diagram for a database**
<img src= bookmanager/static/images/erdplus-diagram-db.jpg>

**Database design**
<img src= bookmanager/static/images/powerpoint-table-db.jpg>

## TESTING 

**Issues with extensions:**

When I started the project I did it with Visual Code; I had an issue with posgress while I was using Visual Studio for the project. Everytime I was typing psql in the terminal and I add the password, I was receiving an error. I had to search on the internet and I found out that I should have type this command instead: psql -U postgres.

Then I moved in Gitpod and I have some issues while I was trying to import my db. I was using the wrong template, instead of using the Gitpod template I was using the Codeanywhere one. I copied all my work and I had to create a new repository.

**Trying to insert values to a table:**

While testing my tables by adding new values, I encountered an error in my terminal: "sqlalchemy.exc.InvalidRequestError: When initializing mapper mapped class Users->users, expression 'Review' failed to locate a name ('Review'). If this is a class name, consider adding this relationship() to the -class 'bookmanager.models.Users'- class after both dependent classes have been defined." I resolved it by rearranging the tables. The first table should have been Review, followed by Users and Book. Python reads the files from top to bottom, so it does not recognize something exists until it reaches that point in the file.

**Trying to create an User login**

I was unsure how to create a user login or sign-up initially because it was my first time working with Flask. After trying various methods I found on the internet, I sought help from a Tutor Assistant at Code Institute.
They suggested adding the following code to my app.route:

  
    if request.method == "POST":
        email = request.form.get("id_email")
        password = request.form.get("password")

        user = Users.query.filter_by(id_email=email).first()

        if user and user.check_password(password):
            #user exists
            return redirect(url_for('profile'))
        else:
            flash("Invalid email or password")

    return render_template("signin.html")

Even though I had the code, I found it challenging to grasp the next steps. Fortunately, I sought support from another student in Slack. They helped me understand that I should import the following: 
"from werkzeug.security import generate_password_hash, check_password_hash ", we used it to protect the password from other users.

**Adding information to a table**

The first database I created was called 'librarymanager', but I encountered some issues while updating the table. As a result, I had to create another database named 'bookmanager'.

## DEPLOYMENT

### Github

This project is deployed using GitHub pages using the following process:

**Deploying a GitHub Repository via GitHub Pages**

1. In your Repository section, select the Repository you wish to deploy.
2. In the top horizontal Menu, locate and click the Settings link.
3. Inside the Setting page, around halfway down locate the GitHub Pages Section.
4. Under Source, select the None tab and change it to Master and click Save.
5. Finally once the page resets scroll back down to the GitHub Pages Section to see the following message *"Your site is ready to be published at (Link to the GitHub Page Web Address)"*. It can take time for the link to open your project initially, so please don't be worried if it down not load immediately.

**Forking the Github Repository**

You can fork a GitHub Repository to make a copy of the original repository to view or make changes without it affecting the original repository.

- Find the GitHub repository.
- At the top of the page to the right, under your account, click the Fork button.
- You will now have a copy of the repository in your GitHub account.
  
**Making a Local Clone**

1. Find the GitHub Repository.
2. Click the Code button
3. Copy the link shown.
4. In Gitpod, change the directory to the location you would like the cloned directory to be located.
5. Type git clone, and paste the link you copied in step 
6. Press Enter to have the local clone created.

[Web link once deployed](https://we-love-reading-ae7806d31b04.herokuapp.com/)
### HEROKU and ELEPHANTSQL
Deploying a Python application on Heroku involves several steps. Here's a general guide:
If you don't have a Heroku account, sign up for one at Heroku's website.
1. Create an account with ElephantSQL
2. Authorise ElephantSQL with your selected GitHub account
3. In the Create new team form:
   - Add a team name (your own name is fine)
   - Read and agree to the Terms of Service
   - Select Yes for GDPR
   - Provide your email address
   - Click “Create Team”
4. Your account is successfully created!
Create a database
5. Click “Create New Instance”
6. Set up your plan (give a name, select the tiny turtle plan and Irish region)
7. Select data center near you (Ireland)
8. Then, click Review
9. Check your details are correct and then click “Create instance”
10. Return to the ElephantSQL dashboard and click on the database instance name for this project
11. In the URL section, clicking the copy icon will copy the database URL to your clipboard
12. Leave this tab open, we will come back here later

Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:

- A requirements.txt file which contains a list of the Python dependencies that our project needs in order to run successfully.

- A Procfile which contains the start command to run the project.
**Process**
1. Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory

 pip freeze --local > requirements.txt

2. Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it

3. Inside the file, add the following command:

 web: python run.py

4. Open your init file

5. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.

 app = Flask(__name__)
 app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

 if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
 else:
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

6. To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:

 if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
 else:
     uri = os.environ.get("DATABASE_URL")
     if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
     app.config["SQLALCHEMY_DATABASE_URI"] = uri
7. Save all your files and then add, commit and push your changes to GitHub

**Heroku process**

Now that you have your database and code in your IDE configured, we will add it to a Heroku app using a new environment variable (Config Var) called DATABASE_URL. Then our Heroku app will be able to connect to the external database.

1. Log into Heroku.com and click “New” and then “Create a new app”
2. Choose a unique name for your app, select the region closest to you and click “Create app”
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var. The result should look something like this:
<img src= bookmanager/static/images/heroku-env-vars.png>

**Deploy the app**

1. Navigate to the “Deploy” tab of your app
2. In the Deployment method section, select “Connect to GitHub”
3. Search for your repo and click Connect
4. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository.
5. As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch. This will start the build process. 
6. Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console”.
7. Type python3 into the console and click Run
8. This opens the Python terminal, in the same way as it would if we typed python3 into the terminal within our IDE. Let’s now create the tables with the commands we used before.
9. Exit the Python terminal, by typing exit() and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.

## HTML AND CSS VALIDATOR
### HTML
**Base.html**
<img src= bookmanager/static/images/check-base-html.png>

**Add Review.html**
<img src= bookmanager/static/images/check-addreview-html.png>

**Books.html**
<img src= bookmanager/static/images/check-books-html.png>

**Profile.html**
<img src= bookmanager/static/images/check-profile-html.png>

**Singin.html**
<img src= bookmanager/static/images/check-signin-html.png>

**Singup.html**
<img src= bookmanager/static/images/check-signup-html.png>

### CSS
<img src= bookmanager/static/images/css-validator.png>

### JAVASCRIPT

**Navigation Bar**
<img src= bookmanager/static/images/js-validator-nav.png>

**Books index html page**
<img src= bookmanager/static/images/js-validator-books.png>

### PYTHON

**__init__**
<img src= bookmanager/static/images/python-check-init.png>

**Routes**
<img src= bookmanager/static/images/python-check-routes.png>

**Run**
<img src= bookmanager/static/images/python-check-run.png>

### LIGHTHOUSE
<img src= bookmanager/static/images/lighthouse.png>

## CREDITS
All the code that I have used to create this website was taken from Code Institute learning platform and from the next following sources:

[MATERIALIZE](https://materializecss.com/)

- I used _Materialize 1.0.0_ version, mainly I used the gryd system to build layouts, navigation bar, footer.

[W3SCHOOL](https://www.w3schools.com/)

- I wanted to create a shadow background for the text and images: box-shadow and text-shadow.

[codingnepalweb](https://www.codingnepalweb.com/draggable-image-slider-html-css-javascript/)

- I added a javascript code from this website which I used to create a draggable image slider to books.script.

[GOOGLE FONTS](https://fonts.google.com/)

- Fonts used are comfortaa and potta.

**Craig Hudson Lead**

- I received support from a this student when I was trying to create a login and register app in my routes.py.

