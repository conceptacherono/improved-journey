# improved-journey
#### Here is the landing page of Awards Web App, April 2022.
#### By **Concepta Cherono**
## Description
This is web application that allows you to view different projects that have been posted. You can vote, comment and rate a project. Users can register in order to post their projects.


## Table of contents
+ [Features](#features)
+ [How to install ](#how-to-install)
+ [Emvironment variables](#environment-variables)
+ [Technology Used](#technologies-used)
+ [Behaviour Driven Development](#behavior-driven-development)
+ [Authors Info](#author)
## App screenshot
![Awward-clone](/static/assets/awward_clone.png)
![Awward-clone](/static/assets/profile_api.png)
## Features

- Django 4.0+
- Profile and Projects API endpoints.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.


## Technologies used
- Back-end Framework: Django (Version 4.0.3)
- Front-end Framework: Bootstrap
- Language: Python (Version 3.8.10)

## How to install
Clone this repo, run:
```bash
git clone https://github.com/conceptacherono/improved_journey_django.git
```
Install the required pip in virtual environment, Refer to requirements.txt. Run:
```bash
#Install all dependecies
$ pip install -r requirements.txt
```
Remember to connect to a database and create migrations
```bash
# Make databases and make migrations
$ python manage.py makemigrations 
$ python manage.py migrate 
```
Create django superuser then run server in development
```  bash
$ python manage.py createsuperuser 
#4. Running the application
$ python3 manage.py runserver
```
## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY=''
DJANGO_DEBUG='True'
DB_NAME=DB_NAME
DB_USER=DB_OWNER
DB_PASSWORD=DB_PASSWORD
DB_HOST=*
CLOUDINARY_CLOUD_NAME=CLOUDINARY_NAME
CLOUDINARY_API_KEY=CLOUDINARY_API
CLOUDINARY_API_SECRET=CLOUDINARY_SECRET
```

## Behavior Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Home page | Displays my favourite projects on home page | Users are able to view projects from available categories |
| Project Images on click | Users could view a specific projects larger view modes|  | 


****
## Author

* Design and developed by: [Concepta Cherono](https://github.com/conceptacherono)