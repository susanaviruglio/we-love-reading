# We ❤️ Reading
## Backend Development Milestone Project by Susana Viruglio

[IMAGE FRONT DESIGN HERE] 

Build a book review and recommendation site.


### External User Goals

- Find books they would like to read.

### Site Owner's Goals

- Earn money on each book purchased via a link from the site.

### Potential Features To Include

- Create a web application that allows users to upload details of books, including book name, author name, link to cover image and any other relevant fields. Allow users to write comments about any book and upvote it.
- Create a web application that allows users to upload details of books, including book name, author name, link to cover image and any other relevant fields. Allow users to write comments about any book and upvote it. 

## UX AIMS

- Infinitive


## USERS STORIES

1. **How can I write a review?** I would like to write a review about my favourite book.

## ADVANCED POTENTIAL FEATURE

- Add a link such as the following to each book page, such that you could conceivably earn money from people looking to buy the book: https://www.amazon.com/s?tag=faketag&k=alice+in+wonderland 

## DESIGN EVOLUTION



## TESTING 

Issues with extensions:

When I started the project I did it with Visual Code; I had an issue with posgress while I was using Visual Studio for the project. Everytime I was typing psql in the terminal and I add the password, I was receiving an error. I had to search on the internet and I found out that I should have type this command instead: psql -U postgres.

Then I moved in Gitpod and I have some issues while I was trying to import my db. I was using the wrong template, instead of using the Gitpod template I was using the Codeanywhere one. I copied all my work and I had to create a new repository.

Trying to insert values to a table:
While I was trying to test my tables by adding new values, I was receiving an error in my terminal: "sqlalchemy.exc.InvalidRequestError: When initializing mapper mapped class Users->users, expression 'Review' failed to locate a name ('Review'). If this is a class name, consider adding this relationship() to the -class 'bookmanager.models.Users'- class after both dependent classes have been defined." I resolved it by moving the tables around, my first table should have been Review, then Users and Book. Python reads the files from top to bottom, so it does not know something exists until it reaches that point in the file.

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
5. Type git clone, and paste the link you copied in step 3.
6. Press Enter to have the local clone created.

[Web link once deployed]

## HTML AND CSS VALIDATOR


## CREDITS

