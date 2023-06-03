## Section 47: A Receipe for Problem Solving

#### Table of Contents
- Introduction
- Step 1 - Understand the problem
- Step 2 - Examples
- Step 3 - Break it Down
- Step 4 - Solve or Simplify
- Step 5 - Look Back and Refactor



### Introduction
- Understand the problem 
- Explore examples
- Break it down
- Solve/simplify
- Look back refactor


### Step 1 - Understand the problem
1. Can we restate the problem in our own words?
2. What are the inputs that go into the problem?
3. What are the outputs that come from the problem?
4. Can the outputs be determined from the inputs? In other words, 
do we have enough information to solve this problem?
5. What should I label the important piece of data
that are part of the problem?

**Example**
Write a function that takes two numbers and returns their sum
1. Can we restate the problem in our own words?
   - Implement addition
2. What are the inputs that go into the problem?
   - Integer? Float? Or?
3. What are the outputs that come from the problem?
   - Integer? Float? Or?
4. Can the outputs be determined from the inputs? In other words, 
do we have enough information to solve this problem?
   - Yes
5. What should I label the important piece of data
that are part of the problem?
   - Add, Sum.



### Step 2 - Examples
1. Start with simple examples
2. Progress to more complex examples
3. Explore examples with empty
4. Explore examples with invalid inputs

**Example**
Write a function which takes in a string and returns count of
each character in the string
```python
# Step 1: simple examples
charCount("bbbb")
#{b: 4}
charCount("hello")
#{h: 1, e:1, l:2, o:1}

# Step 2: complex examples
charCount("My name is Lewis")

# Step 3: empty
charCount("")

# Step 4: invalid inputs
charCount(1)

def charCount(text: str) -> dict:
    if not isinstance(text, str):
        return "Input type must be string"
    my_dict = {}
    for i in text:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict
```


### Step 3 - Break it Down
Write out the steps that you need to take
```python
charCount("My name is Lewis")
#{
#    'M': 1, 
#    'y': 1, 
#    ' ': 3, 
#    'n': 1, 
#    'a': 1, 
#    'm': 1, 
#    'e': 2, 
#    'i': 2, 
#    's': 2, 
#    'L': 1, 
#    'w': 1
#}

def charCount(text:str):
    # declare an object to return at the end
    # loop over the string
        # if the char is letter and it is in out object, 
        # add one to the value
        # if the char is letter and it is not in our object, 
        # add that char to our object with the value of one
    # return an object
```


### Step 4 - Solve or Simplify
#### Solve the problem
#### If you cannot...
#### Simplify the problem
- Find the core difficulty
- Temporarily ignore that difficulty
- Write a simplified solution
- Then incorporate that difficulty
```python
def charCount(text:str):
    # declare an object to return at the end
    result = {}
    # loop over the string
    for i in text.lower():
        # if the char is lowercase letter and it is in out object, 
        # add one to the value
        if i in result:
            result[i] += 1
        # if the char is letter and it is not in our object, 
        # add that char to our object with the value of one
        else:
            result[i] = 1
    # return an object
    return result
```

### Step 5 - Look Back and Refactor
- Can we check the result?
- Can we drive the result differently?
- Can we understand it at a glance?
- Can we use the result or method for some other problem?
- Can you improve the performance of your solution?
- How other people solve this problem?

```python
def charCount(text:str):
    # declare an object to return at the end
    result = {}
    # loop over the string
    for i in text.lower():
        # if the char is lowercase letter and it is in out object, 
        # add one to the value
        if isinstance(i, str) and not (i.isspace()):
            if i in result:
                result[i] += 1
            # if the char is letter and it is not in our object, 
            # add that char to our object with the value of one
            else:
                result[i] = 1
    # return an object
    return result
```

#### Summarize
- Understand the problem 
- Explore examples
- Break it down
- Solve/simplify
- Look back refactor