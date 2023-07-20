## 05 Flask-Smorest for more efficient development

#### Table of Contents
- Data model with improvements for our API
- General improvements to our first RESET API
- New endpoints for our first REST API
- How to run the API in Docker with automatic reloading and debug mode
- How to use Blueprints and MethodViews in Flask
- How to write mashmallow schemas for our API
- How to perform data validation with mashmallow
- Decorating responses with Flask-Smorest

### How to run the API in Docker with automatic reloading and debug mode
Refer to `Dockerfile` for commands. 

First build the app image
```
docker build -t flask-smorest-api .
```
We are going to replace the contents of the app directly in the image with this
folder that we are currently in. We use `-w /{WORKDIR}` (`/app` in our case)to do so. Whenever we make a change to our code in `/{WORKDIR}` folder, the code will be changed in the running container too. 
We then add a volume with `-v "$(pwd):/{WORKDIR}`, so that Docker creates a volume, 
which is a mapping of a directory between your local file system and the container's file system.  
```
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
```

### Swagger-UI
[localhost:5005/swagger-ui](localhost:5005/swagger-ui)

### New Dictionary Merge and Update Operator
[Dictionary Merge and Update Operators in Python 3.9](https://blog.teclado.com/python-dictionary-merge-update-operators/)