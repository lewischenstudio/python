## 04 Introduction to Docker
##### Table of Contents
- What are Docker containers and images
- How to run a Flask app in a Docker container

### What are Docker containers and images

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