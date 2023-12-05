# We ❤️ Reading
## Backend Development Milestone Project by Susana Viruglio

[IMAGE FRONT DESIGN HERE] 

Build a book review and recommendation site.


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

While I was trying to test my tables by adding new values, I was receiving an error in my terminal: "sqlalchemy.exc.InvalidRequestError: When initializing mapper mapped class Users->users, expression 'Review' failed to locate a name ('Review'). If this is a class name, consider adding this relationship() to the -class 'bookmanager.models.Users'- class after both dependent classes have been defined." I resolved it by moving the tables around, my first table should have been Review, then Users and Book. Python reads the files from top to bottom, so it does not know something exists until it reaches that point in the file.

**Trying to create an User login**

I was not sure how to create an user login or log up at the beginning because it was the first time that I was working with Flask. So, after trying different methods I found on the internet, I asked for help in Tutor Assistant in Code Institute. He suggested to add this code in my app.route:

  
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

Even though I had this code, I found it hard to understand the next steps, so I found support from another student in Slack. He helped me to understand that I should I have imported:
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

[Web link once deployed]

## HTML AND CSS VALIDATOR


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

