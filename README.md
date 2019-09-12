# Concerts Finder
> Concerts Finder is a website created with Django. You can find concerts with various options but if you can't find anything what you need, you can show your interest.
All you got to do is to like a dream concert from the list or add any concert invented by you to the list of dream concerts.

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## Technologies
* Python - version 3.6
* Django - version 2.2.4
* PostreSQL - version 10.10

## Setup
* Clone git repository
* Create virtualenv 'virtualenv -p python3 venv'
* Activate virtualenv 'source venv/bin/activate'
* Install requirements 'pip install -r requirements.txt'
* Setup psql database called 'concerts_db'
* Change psql user and password to yours
* 'python manage.py migrate'
* 'python manage.py runserver'

## Features
List of features ready and TODOs for future development
* Landing page as a carousel with the most popular concerts
* Searching concerts by an artist's name, a band's name, city and date
* Lists of all concerts and top 10
* Concert details with event page on Facebook
* Possibility to like concerts (option for logged in users only)
* Dream concerts - if you can't find any interesting events, you can show your interest by liking dream concerts or adding any concert invented by you to the list of dream concerts (option for logged in users only)

To-do list:
* Adding and editing list of concerts
* Login/Logout
* REST API

## Status
Project is: _in progress_
