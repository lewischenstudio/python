## Section 11: Deployments with Render.com

#### Table of Contents
- Creating a Render.com web service
- How to run Flask with Gunicorn in Docker
- Get a deployed PostgreSQL database
- Use PostgreSQL locally and in production
- Test the finished production app


### How to run Flask with Gunicorn in Docker
Dockerfile
```docker
FROM python:3.10
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
```
Docker command line
```
docker run -dp 5000:5000 -w /app -v $(pwd):/app IMAGE_NAME sh -c "flask run -host 0.0.0.0"
```