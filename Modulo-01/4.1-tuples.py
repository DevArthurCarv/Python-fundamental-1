#TUPLAS

"""
A tuple is an immutable and ordered data structure 
that allows you to store a collection of elements. 
The elements of a tuple are enclosed in 
parentheses (), separated by commas.
"""

point = (3, 4)

print(point[0])  # print 3
print(point[1])  # print 4

"""
Unlike lists, tuples are immutable, meaning they 
cannot be modified once created. You cannot add, 
delete, or change elements in an existing tuple.

Tuples are useful when you need to store a 
collection of elements that should not be modified, 
such as coordinates or configuration data.
"""

#Tuple methods

"""
Although tuples are immutable, Python provides 
several useful methods for working with them:

count(element): returns the number of times an 
element appears in the tuple.

index(element): returns the index of the first 
appearance of an element in the tuple. Optionally, 
you can specify the start and end of the search.

len(tuple): although not a tuple method per se, 
this built-in function returns the length of the 
tuple.
"""

my_tuple = (1, 2, 3, 2, 4, 2)

print (my_tuple.index(2)) # Output: 1










