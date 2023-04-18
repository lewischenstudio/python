# REST APIs with Flask and Python in 2023

## [Course Link](https://www.udemy.com/course/rest-api-flask-and-python/)

## Course Certificate


# Flask REST API

## Install Flask
Set up the Python Virtual Environment in a directory of your choice.
```
python3.9 -m venv venv
venv/scripts/activate
pip install flask
```

## Section Content
In this section we'll make a simple REST API that allows us to:
- Create stores, each with a name and a list of stocked items.
- Create an item within a store, each with a name and a price.
- Retrieve a list of all stores and their items.
- Given its name, retrieve an individual store and all its items.
- Given a store name, retrieve only a list of item within it.

## The First Endpoint
Create the app.py file and run the Flask command.
```
flask run
```

## What is JSON?
JSON is just a string whose contents follow a specific key-value format.

# Docker

## Create Dockerfile

## Docker Build
```
docker build -t rest-apis-flask-python .
```

## Docker Run
```
docker run -d -p 5000:5000 rest-apis-flask-python
```
