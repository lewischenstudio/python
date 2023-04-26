# 03 Your First REST API

##### Table of Contents
- Access the course e-book here
- Overview of the project we'll build
- Initial set-up for a Flask app
- Your first REST API endpoint
- What is JSON?
- How to interact with and test your REST API
- How to create stores in our REST API 
- How to create items in each store
- How to get a specific store and its items

### Initial Setup for a Flask app
Create a Python Virtual Environment
```
python3.10 -m venv .venv
. venv/bin/activate (Mac or Linux)
venv/scripts/activate (Windows)
```
Install Flask
```
pip install flask
```
Run Flask
```
flask run
```

### What is JSON?
JSON is just a string whose contents follow a specific key-value format.
```json
{
    "key": "1",
    "name": "Lewis",
    "grade": 88,
    "pass": true,
    "students": ["Lewis", "Mike"],
    "meta": {"time": "2020-01-03"}
}
```
We have the following in the above JSON
- Strings
- Numbers
- Booleans
- Lists
- Objects (dictionaries in Python)


### How to interact with and test your REST API
[Insomnia](https://insomnia.rest) \
[Postman](https://postman.com)


