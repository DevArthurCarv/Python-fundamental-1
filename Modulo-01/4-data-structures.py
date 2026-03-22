# LISTS

"""
A list is a mutable and ordered data structure that 
allows you to store a collection of elements. 
The elements of a list can be of different data 
types and are enclosed in square brackets [], 
separated by commas.
"""


fruts = ["apple", "banana", "orange"]

print(fruts[0]) #print "apple"
print(fruts[1]) #print "banana"
print(fruts[2]) #print "orange"


# LIST METHODS

"""
Lists in Python have several built-in methods that allow us to manipulate and 
modify list elements. Some common methods are:

append(element): adds an element to the end of the list.
insert(index, element): inserts an element at a specific position in the list.
remove(element): removes the first occurrence of an element in the list.
pop(index): removes and returns the element at a specific position in the list.
sort(): sorts the elements of the list in ascending order.
reverse(): reverses the order of the elements in the list.
"""

"""
fruts = ["apple", "banana", "orange"]

fruts.append("pear")
print(fruts) #print ["apple", "banana", "orange", "pear"]

fruts.insert(1, "grape")
print(fruts) #print ["apple", "grape", "banana", "orange", "pear"]

fruts.remove("banana")
print(fruts) #print ["apple", "grape", "orange", "pear"]

fruts_removed = fruts.pop(2)
print(fruts) #print ["apple", "grape", "pear"]
print(fruts_removed) #print ["orange"]

fruts.sort()
print(fruts) #print ['apple', 'grape', 'pear']

fruts.reverse()
print(fruts) #print ['pear', 'grape', 'apple']
"""


# LISTA COMPREHENSIONS

"""
List comprehensions are a concise way to create new lists based on an 
existing sequence. They allow you to filter and transform the elements 
of a list in a single line of code.
"""

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares) #print [4, 16]


"""
In this example, a new list called "squares" is 
created, containing the squares of the even numbers 
from the "numbers" list. The expression x ** 2 
squares each element, and the condition if x % 2 == 0 
filters out only the even numbers.
"""






