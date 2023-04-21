## 10 Working in Threads with Python

The following topics will be covered in this chapter:
- The concept of a thread in the context of concurrent programming in computer science
- The basic API of the threading module in Python
- How to create a new thread via the threading module
- The concept of a lock and how to use different locking mechanisms to synchronize threads
- The concept of a queue in the context of concurrent programming, and how to use the Queue module to work with queue objects in Python

### Thread
A thread of execution is the smallest unit of programming commands (code) that a scheduler (usually as part of an operating system) 
can process and manage.

### Threads versus processes
- A thread is typically a component of a process, so a process can have multiple threads.
- Threads also usually allow for shared resources, such as memory and data, 
while it is fairly rare for processes to do so.


### Multithreading
- Single-threading is similar to traditional sequential processing.
- Multithreading implements more than one thread to exist and execute in a single process
simultaneously.
- Time slicing is a technique that allows the CPU to switch between different software running on
different threads.
- Systems with multiple processors or cores can easily implement multithreading, by executing each
thread in a separate process or core, simultaneously.

#### Advantages
- One of the main advantages of concurrency through multithreading is speedup in execution time.
- A multithreaded program can provide better responsiveness by using separate threads to perform
computation and remain running to take in different user input simultaneously.
- Multithreaded programs use significantly fewer resources than would be needed when using
single-threaded or multiprocess programs.

### Disadvatanges
- Even though a process can contain multiple threads, a single illegal
operation within one thread can negatively affect the processing of all of the
other threads in the process, and can crash the entire program as a result.
- Unintuitive problems that can be caused by careless thread coordination include deadlocks, livelocks, and race conditions, leading to sychronization problems.

### Remarks
- Execution times for multiple threads can vary regardless their starting times. This phenomenon is
direct result of concurrency via multithreading; since the two threads were initialized and started
almost simultaneously, it was quite likely for one thread to get ahead of the other in execution.

### The threading Module
The `threading` module in Python 3 is designed to be user-friendly for those that come from the object-oriented software development paradigm, treating each thread that is created as an object.

- `thread.start_new_thread()` takes in a separate function as its main argument, in order to spawn a new thread.
- `threading.activeCount()` returns the number of currently active thread objects in the program
- `threading.currentThread()` returns the number of thread objects in the current thread control from the caller
- `threading.enumerate()` returns a list of all the currently active thread objects in the program

The `threading` module also provides a Thread class that supports the object-oriented implementation of threads.
- `run()` is executed when a new thread is initialized and started
- `start()` starts the initialized calling thread object by calling the `run()` method
- `join()` waits for the calling thread object to terminate before continuing to the execute the rest of the program
- `isAlive()` returns a Boolean value, indicating whether the calling thread object is currently executing
- `getName()` returns the name of the calling thread object
- `setName()` sets the name of the calling thread object


### Starting a thread with the thread module
`thread.start_new_thread(function, args[, kwargs])`
- the `function` parameter is the name of the function
- the `args` parameter list includes the arguments to be passed to the function
- `example2.py`
- The thread terminates silently before running the function
- Workaround: use `input()` to prevent the program from exiting until the user presses any key


### Starting a thread with the threading module
To create and customize a new thread using the threading module, there are specific steps that need to be followed:
- Define a subclass of the `threading.Thread` class in your program
- Override the default `__init__(self [,args])` method inside of the subclass, in order to add custom arguments for the class
- Override the default `run(self [,args])` method inside of the subclass, in order to customize the behavior of the thread class when a new thread is
initialized and started
- `example1.py`
- `example3.py`
- No more workaround to make sure that all of the threads have finished executing successfully in this `threading` module, in terms of functionality and high-level API calls.


### Thread synchronization
Thread/process synchronization is a concept in computer science that specifies various mechanisms to ensure that no more than one concurrent thread/process can process and execute a particular program portion at a time; this portion is known as the **critical section**.

### The threading.Lock class
The `threading.Lock` class provides an approach to creating and working with locks, in order to apply thread synchronization.
- `threading.Lock()` initializes and returns a new lock object.
- `acquire(blocking)` makes sure that all of the threads will run synchronously (that is, only one thread can execute the critical section at at time).
  - The optional argument `blocking` allows us to specify whether the current thread should wait to acquire the lock
  - When `blocking = 0`, the current thread does not wait for the lock and simply returns 0 if the lock cannot be acquired by the thread, or 1 otherwise.
  - When `blocking = 1`, the current thread blocks and waits for the lock to be released and acquires it afterwards
- `release()` releases the lock.
- `example4.py`


### Queues
A queue is an abstract data structure that is a collection of different elements maintained in a specific order.
- `enqueue` is a method to add elements to the end of the queue.
- `dequeue` is a method to remove elements from the beginning of the queue.
- **First In First Out (FIFO)**: elements that are added first will be removed first
- **Last In First Out (LIFO)**: elements that are added last will be removed first. Stack
- Empty queue and full queue

### The Python queue module
The `queue` module in Python provides a simple implementation of the queue data structure.
- `get()` returns the next element of the calling queue object and removes it from the queue object
- `put()` adds a new element to the calling queue object
- `qsize()` returns the number of current elements in the calling queue object (that is, its size)
- `empty()` returns a Boolean, indicating whether the calling queue object is empty
- `full()` returns a Boolean, indicating whether the calling queue object is full

### Queueing in concurrent programming
- It could be more beneficial to have a fixed number of threads (commonly known as a thread pool) that
would work through the tasks in a cooperative manner.
- Use **task queue** to send elements to the thread pool to process.
- `example5.py` shows the structure that where task queue that holds all the tasks to be executed and
a thread pool (threads A, B, and C) that interacts with the queue to process its elements individually.

### Multithreaded priority queue
We need to redefine or change the order of the elements dynamically. This is where the concept of priority
queuing comes in handy. Each of the elements in the **priority queue** has a priority associated with it
or needs to specify its priority. Elements with higher priorities are processed before those with lower priorities.
- Bandwidth management is the system where prioritized traffic, such as real-time streaming, is processed with the
least delay and the least likelihood of being rejected.
- Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph. Using
the priority queue can lead to faster computing times than using a basic queue.
- Best-first search algorithms are used to find the shortest path between two given nodes of a graph.
A priority queue is implemented to keep track of unexplored routes; the routes with shorter estimated path
lengths are given higher priorities in the queue.

Exercises
1. What is a thread? What are the core differences between a thread and a process? \
  A thread of execution is the smallest unit of programming commands. The core difference between a thread and
  a process is that a process can contain multiple threads.Multithreading implements more than one thread to 
  exist and execute in a single process simultaneously.

2. What are the API options provided by the thread module in Python? \
  The `thread` module in Python has the following API options.
    - `thread.start_new_thread()` takes in a separate function as its main argument, in order to spawn a new thread.
    - `threading.activeCount()` returns the number of currently active thread objects in the program.
    - `threading.currentThread()` returns the number of thread objects in the current thread control from the caller.
    - `threading.enumerate()` returns a list of all the currently active thread objects in the program.


3. What are the API options provided by the threading module in Python? \
  The `threading` module also provides a Thread class that supports the object-oriented implementation of threads.
    - `run()` is executed when a new thread is initialized and started.
    - `start()` starts the initialized calling thread object by calling the `run()` method.
    - `join()` waits for the calling thread object to terminate before continuing to the execute the rest of the program.
    - `isAlive()` returns a Boolean value, indicating whether the calling thread object is currently executing.
    - `getName()` returns the name of the calling thread object.
    - `setName()` sets the name of the calling thread object.

4. What are the processes of creating new threads via the thread and threading modules? \
  - Starting a thread with the `thread` module involves using the API `thread.start_new_thread(function, args[, kwargs])`.
  - Starting a thread with the `threading` module involves three steps. First, define a subclass of the `threading.Thread` class
  in your program. Secondly, override the default `__init__(self [,args])` method inside of the subclass, in order to add custom
  arguments for the class. Lastly, override the default `run(self [,args])`.


5. What is the idea behind thread synchronization using locks? \
Thread/process synchronization is a concept in computer science that specifies various mechanisms to ensure that no more than one
concurrent thread/process can process and execute a particular program portion at a time, also known as critical section. The
`threading.Lock` class provides an approach to creating and working with locks, in order to apply thread synchronization.

6. What is the process of implementing thread synchronization using locks in Python? \
To implement thread sychronization using locks in Python, we can use `threading.Lock()` to initialize and return a new lock object.
Then use `acquire(blocking)` to sure that all of the threads will run synchronously (that is, only one thread can execute the critical
section at at time). The optional argument `blocking` allows us to specify whether the current thread should wait to acquire the lock.
When `blocking = 0`, the current thread does not wait for the lock and simply returns 0 if the lock cannot be acquired by the thread,
or 1 otherwise. When `blocking = 1`, the current thread blocks and waits for the lock to be released and acquires it afterwards. Use
`release()` to releease the lock.

7. What is the idea behind the queue data structure? \
The queue data structure is a collection of different elements maintained in a specific order so that elements that are added 
first will be removed first (FIFO).

8. What is the main application of queuing in concurrent programming? \
The main application of queueing in concurrent programminng is to allow a fixed number of threads (thread pool) work through the tasks
in a cooperative manner, where the task queue holds all the tasks to be executed the FIFO manner and the thread pool interacts with
the queue to process its elements individually.

19. What are the core differences between a regular queue and a priority queue? \
Each of the elements in a **priority queue** has a priority associated with it or needs to specify its priority,
but a regular queue doesn't have priority associated with its elements.