# callable
from pprint import pprint
import os
print(callable(pprint))    # True
pprint(dir(os)) # TypeError: 'str' object is not callable
# print(os.name())    # get the name of the operating system - # TypeError: 'str' object is not callable
print(callable(os.name))    # check if the os module is callable = False
