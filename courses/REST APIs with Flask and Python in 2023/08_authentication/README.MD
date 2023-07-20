## Section 8: User authentication with Flask-JWT-Extended

#### Table of Contents
- What is a JWT
- Who uses a JWT
- How to set up Flask-JWT-Extended with our app
- Coding the User model and schema
- How to add a register endpoint to the REST API
- How to add a login endpoint to the REST API
- Protect endpoints by requiring a JWT
- JWT claims and authorization
- How to add logout to the REST API
- Request chaining with Insomnia
- Token refreshing with Flask-JWT-Extended


### What is a JWT

[Introduction to JSON Web Tokens](https://jwt.io/introduction)

### Who uses a JWT
#### Getting an access token
- The client sends authentication information to the API
(usually username and password)
- The API validates them and generates an access token (in our case, a JWT)
- Inside the JWT, the user's unique ID is stored
- The access token is sent back to the client for storage and later use (i.e., cookies, local storage)

#### An example of using access tokens
- Imagine you're making an API with an endpoint, `/my-info`, which should return information about the currently logged-in user
- Imagine the client is a website. In the website there is a button,
"See my info", which when clicked sends a request to `/my-info` to get the information
- Let's say a user arrives at the website without having logged in. What does the flow look like?
  - Access website
  - Click "See my info"
  - The client sends a request to API `/my-info` endpoint
  - The API looks at access token and notices it is missing
  - The API responds with authentication error to the client
  - The client receives the error
  - The client redirects the user to login page
  - The user fills in the username and password on the login page
  - The client sends username and password to API `/login` endpoint
  - The API checks the username and password are valid
  - The API generates access token JWT, including the user's ID 
  - The API responds the client with the access token
  - The client receives the access token and stores it somewhere
  - The user clicks on "See my info" button again
  - The client sends request to API `/my-info` endpoint with the access token
  - The API looks at the access token and decodes it
  - The API loads the user data from the database using the user's ID in the access token
  - The API responds with user's information to the client 
  - The client shows the user's information as received from the API

[The workflow diagram](https://rest-apis-flask.teclado.com/assets/images/my-info-flow.drawio-e9ca9f4a6cb7789c88884321fdcdcba8.png)

#### How long do JWTs last for, or how often do users need to authenticate?
- Access tokens don't last forever, as that would be a security risk (e.g., if the user forgets to log out in a shared computer).
- Shorter expiry times are safer, but if users have to re-authenticate every few minutes, it's incredibly annoying
- This is where token refreshing comes into play.


#### Virtual Machine
Hardware -> MacOS -> Hypervisor -> Windows VM -> Windows app(s)

#### Docker Containers
Hardware -> Linux -> Docker -> Docker(s) -> Container process

#### What is a Kernel?
- An Operating System is made up of two main parts: the kernel and files/programs.
- The kernal usually interacts with and controls the hardware.

#### To run Linux containers on Windows/macOS
You first need to run a Linux VM
Docker Desktop takes care of this for you, but it's inefficient

#### What does a Docker container run?
It runs everything but the kernel. Docker containers are based on images, which 
specify what is inside the container when it runs.

- The OS is made up of kernel + applications
- Any applications from the OS you want to use need to be included in the 
container (e.g. Bash, curl, etc.)
- You also need to include Python, pip, and install dependencies your app needs


#### What is a Docker image?
- A snapshot of source code, libraries, dependencies, tools and everything else
(except the Operatying system kernel) that a container needs to run.
- There are many pre-built ones, so we don't need to build them from scratch.

#### The Dockerfile
- A definition of a Docker image.
- We use Dockerfiles to build images.
- We can use an image to run one or more containers.


### How to run a Flask app in a Docker container
- Install Docker Desktop from [Docker](https://docker.com)
- Write the Dockerfile
- Build a Docker image with tag name "rest-apis-flask-python" in our current directory `.`.
  ```
  docker build -t rest-apis-flask-python .
  ```
- Run the Docker container in the detached mode (`-d`) and port 5005 with the following command line
  ```
  docker run -dp 5005:5000 rest-api-flask-python
  ```