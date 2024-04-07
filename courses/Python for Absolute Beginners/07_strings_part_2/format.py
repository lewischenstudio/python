"""
Python .format()
"""

name = input("What is the job applicant's name? ")
degree = input("What is their major at college? ")
job = input("What is their current occupation? ")
experience = input("How many years have they been working in their field? ")

print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

print(f"{name} majored in {degree}, works as a {job}, and has {experience} years of experience.")