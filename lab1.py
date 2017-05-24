# Lab: Basic Join

###### Delivery Method: Doctest

##### Goal

#Write a function that convert two input strings into kebab-case sting output.
#
#
###### Instructions
#
#Use the the `str.join()` method.
#
#-------------------
##### Documentation
#
###### [Python Official Docs: str.join()](https://docs.python.org/3.6/library/stdtypes.html#str.join)
#-------------------------------------------
#
#### Advanced
#
#  - Implement a solution that employs a dictionary
#  - Write an additional doctest and execute it

first = input('What\'s the first string? ')
second = input('What\'s the second string? ')
print(str.join(first, second))
