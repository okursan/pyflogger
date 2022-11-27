# PyFlOGGER
#### Video Demo:  https://youtu.be/EvfQ6rcM6ZI
#### Description:

# PyFlOGGER
## Yet Another Personal Blog Scriprt Written in Python
### with the power of Flask & SQLAlchemy

I have created a weblog script for my final project. It is written in Python Flask. The database is SQLite. **PyFlogger** is a microblog compared to well-known blog scripts (Wordpress , etc.). It has a twitter-like post system. But post is not limited to any number of characters.

Project files is in *blogsite* directory. The *app.py* in the main dir calls blog script some kind of a modular way.

*__init__.py* file handles initialization for our app. Provides database connection thourough SQLAlchemy. Registers view files. Loads models and user management system.

*models.py* contains database models. There are 4 models in this projects. Each has its own corresponding table in the database. They manage crud database operations with SQLAlchemy.

There are 3 view files in this project. View files are the connection between user requests and databases. They handle what will be seen on each page.

*auth.py* is for login management. This project is closed for anonymouse registers. Because it is a personal blog script. So, only website owner or whom admin lets can login. 

*views.py* is front-end view file. main page, category main page and post pages are handled with this file.

*dashboard.py* is back-end view file. All administrative stuff is handled with this file.

*templates* folder contains html files. They are coded with html and Jinja template codes.