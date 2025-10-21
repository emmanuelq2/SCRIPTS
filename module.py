# random
import random

# random.randint(a, b) returns a random integer N such that a <= N <= b.
r = random.randint(0,9)
print(r)

# random.uniform(a, b) returns a random floating point number N such that a <= N <= b.
u = random.uniform(0,1) # decimal number between 0 and 1
print(u)

# random.randrange(start, stop[, step]) returns a randomly selected element from range(start, stop[, step]).
range = random.randrange(999)
print(range)
range = random.randrange(0,9)
print(range)
range = random.randrange(0, 100, 2) # start, end, step
print(range)

print(dir(random))
help(random)


# exercise
a = random.randint(0,100)
print(a)
b = random.randint(0,100)
print(b)

if a > b:
    print("Le nombre a est plus grand que le nombre b.")
elif a < b:
    print("Le nombre b est plus grand que le nombre a.")
elif a == b:
    print("Le nombre a et le nombre b sont égaux.")

# os module
import os
patch = "C:/Documents/CLASS/UDEMY/PYTHON"
folder = os.path.join(patch, "folder")  # join the path with the file name
if not os.path.exists(folder): # check if the directory exists
    os.makedirs(folder) # create a directory
else:
    print("The folder already exists")

# second option
# os.makedirs(folder, exist_ok=True) # create a directory

if not os.path.exists(folder): # check if the directory exists
    os.rmdir(folder) # remove a directory

pwd = os.getcwd() # get the current working directory
print(pwd)


# pprint(dir(random)) # print the list of attributes and methods of the random module
# pprint(dir(os)) # print the list of attributes and methods of the os module
# pprint(help(os)) # print the documentation of the os module

# callable
from pprint import pprint
print(callable(pprint))    # false
print(os.name())    # get the name of the operating system
print(callable(os.name))    # check if the os module is callable
