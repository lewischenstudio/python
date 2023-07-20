# C Performance with Cython

Cython is a language that extends Python by supporting the declaration of types for
functions, variables, and classes. These typed declarations enable Cython to compile
Python scripts to efficient C code. Cython can also act as a bridge between Python and C as it provides easy-to-use constructs to write interfaces to external C and C++ routines.


## Install Packages

In this chapter, we will learn the following things:
- Cython syntax basics
- How to compile Cython programs
- How to use static typing to generate fast code
- How to efficiently manipulate arrays using typed memoryviews
- Optimizing a sample particle simulator
- Tips on using Cython in the Jupyter notebook
- The profiling tools available for Cython

We use Linux Debian system for Cython, and our Python version is 3.8. We install minimal Linux packages required for this module with the following command.
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8 gcc libpython3.8-dev
sudo apt-get install build-essential python3-dev python3.8-venv
sudo apt update
python3.8 --version
```

Install Cython in your virtual environment folder
```
pip install Cython
```

## Basic Tutorial

### PYX file
Create a new hello.pyx file witht he following code:
```python
def say_hello_to(name):
    print("Hello %s!" % name)
```

### C File
Compile the `hello.c` file with Cython command
```
cython hello.pyx
```

### SO file
Compile the `hello.so` file with `gcc`
```
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I/usr/include/python3.8/ -o hello.so hello.c
```
Note that the Python include directory might be different in your system. To find the directory, use the command 
```
python -c "from distutils import sysconfig; print(sysconfig.get_python_inc())"
```

### Python Console
Enter the Python console
```
>>> import hello
>>> hello.say_hello_to("Lewis")
Hello Lewis!
```


## Source

Lanaro, Gabriele, et al. *Advanced Python Programming: Build High Performance, Concurrent, and Multi-Threaded Apps with Python Using Proven Design Patterns*. Packt Publishing, 2019.