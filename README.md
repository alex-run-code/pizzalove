# pizzalove

## What is Pizzalove ? 

Pizzalove is a web application allowing to show how much you love pizza by clicking on a button.
The more you click, the more you progress in the pizza lovers ranking

## How does it work ?

The pizzalove project is using Python and Django. It is separated in 2 applications :

### Homepage

This application is responsible for displaying the front end. Within this application, you'll
find the templates for :
- Login
- Logout
- Signup
- Visiting the homepage
- Voting

The chart displayed is made with chartjs. The frontend is made with bootstrap.
You can access the mainpage by starting the server with :

    py manage.py runserver

and then visiting:

    localhost:8000/home

### Api 

This application is responsable for managing the endpoints. We only have one endpoint for now, /api/like. Here's what it does :
- If requested with a GET method, it'll list the pizza lovers
- If requested with a POST method, it'll create a like for the currently logged user. Only accessible if you're authenticated

## That's it ! 

That's it for now !