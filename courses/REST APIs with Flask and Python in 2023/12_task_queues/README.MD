## Section 12: Task Queues with rq and sending emails

#### Table of Contents
- How to send emails with Python and Mailgun
- How to send emails when users register
- What is a task queue and setting up a Redis database
- How to populate and consume the task queues with rq
- How to process background tasks with the rq worker
- How to send HTML emails using Mailgun and Python
- How to deploy a background worker to render.com


### How to send emails with Python and Mailgun

[Mailgun](https://www.mailgun.com)


### How to process background tasks with the rq worker
Build a Docker image
```
docker build -t rest-api-recording-email .
```

Run a Docker container in a separate terminal
```
docker run -w /app rest-api-recording-email sh -c "rq worker -u rediss://red-ccu1t8aen0hklj27aa10:MnLs0mKAMDwImrX7MBXWRkdrh49s6wrp@frankfurt-redis.render.com:6379 emails"
```

Run the main Docker container 
```
docker run -p 5000:80
```
