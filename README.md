# tick_tack_toe_app
A tic tac toe game build using django and react

This app has been built using the django framework for the management system, and react for the frontend of the tic tac toe game. Games history will be stored in the management.
system and stored in an sql database.

### Django App

### N.B - Changes

#### a. The attributes and methods for calculations have been made in the models.py file and ajax requests in the views.py file

#### b. Html templates are in the templates folder, while css and js files are in the static folder

#### c. Migrations will need to be re-run in order to create the new table

#### d. cd into the tictactoe folder and run : python players.py


1. To use the django app and login to view the history of games, do the following

```
( Make sure you have python 3 installed and pip)
a.Make sure you have a django environment setup along with sql

b. Clone the file : https://github.com/jared7129/tick_tack_toe_app.git

c. cd django_app

d. Run migrations - python manage.py migrate

e. Run the app - python manage.py runserver
```

### Extra packages to install:

```
cors-header
django-rest framework

(You can use pip install to do this)

```

### React App

1. You can run the react part of the app(The frontend) by doing the following

```
a. cd react app

b.Install relevant packages -  npm install

c. Start the app - yarn start

(Make sure you have npm and yarn installed)

```

