# Project: Item Catalog

### About
This project uses concepts from Udacity's Full Stack Foundations and Authentication and Authorization courses to build an item catalog web application. The app catalogs reading lists and books associated with each list. Users can log into the app using Google or Facebook account authorization, create reading lists and add books to the reading lists they create. In addition, the app also features JSON endpoints which allows users to access data in the catalog in a serialized format. The app uses the Flask development framework, SQLAlchemy, and Google and Facebook authorization APIs.

### Directory Contents
The following contents are inside the catalog directory, which is within the vagrant directory:
1. `static/` - Contains the Bootstrap CSS files as well as main.css.
2. `templates/` - Contains the Flask templates used to render HTML on the app's pages.
3. `views/` - Contains Flask Blueprints which powers the functionalities throughout the app.
4. `readinglistwithusers.db` - Database containing information displayed in the app.
5. `database_setup.py` - Provides database schema for readinglistwithusers.db.
6. `database_setup.pyc` - Compiled version of database_setup.py.
7. `lotsoflistsusers.py` - Pre-populates readinglistwithusers.db with initial data which can be displayed in the app.
8. `client_secrets.json` and `fb_client_secrets.json` - JSONs which provide app ID and client secret information for the Google and Facebook authorization APIs.
9. `helpers.py` - Contains import statements and establishes database connection to readinglistwithusers.db for use throughout the app.
10. `helpers.pyc` - Compiled version of helpers.py.
11. `key.py` - Contains secret key used to flash messages in the app.
12. `key.pyc` - Compiled version of key.py.
13. `__init__.py` - Imports the Flask Blueprints and initializes the app.

### How to Run
1. Install Vagrant and VirtualBox. If you need help installing Vagrant and VirtualBox, you can find details here: https://udacity.atlassian.net/wiki/display/BENDH/Vagrant+VM+Installation
2. Clone or download this repo to your computer.
3. Launch the Vagrant virtual machine in Terminal (vagrant up and vagrant ssh).
4. Navigate into the catalog directory and run the following command:
    `python __init__.py`.
5. Access the application by visiting http://localhost:5000 in your web browser.

### Areas for Improvement
You can easily add other authorization methods to the app. You could also update the app to include additional features, like the ability to add comments or reviews to specific books.