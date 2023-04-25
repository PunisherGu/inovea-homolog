# Coodesh Chaleng

This is a challenge proposed by Inovea

## Languages and Frameworks

* Python 3.8
* Django 4.2
* Django Rest Framework 3.14



## Getting Started

This project use Docker for run, so run commands bellow
```python
docker-compose up --build
```
##

If for some reason docker compose doesn't run, try:

```python
1 - Create a virtualenv (we recommend virtualenvwrapper)
2 - Clone this repository
3 - Run: pip install -r requirements.txt
4 - Run: python manage.py migrate
5 - Run: python manage.py runserver
```

##

PS: 
The credentials as well as the secret key are exposed in the code for easier evaluation, obviously in a real environment this would be stored in environment variables

PS2:
For such a simple purpose, the most recommended would be to just use a python approach, but for teaching purposes, I wanted to show the frameworks that I master the most, some configuration and organization tricks