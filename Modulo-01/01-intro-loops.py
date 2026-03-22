"""
In the next few topics, things will be more organized.
I'll create a folder for each topic and link to each 
one in (https://github.com/DevArthurCarv/Python-fundamental-1/blob/main/README.md)
"""

# First code

print("Hello World!!!")
print(82375639)

# A bit of syntax

# This is a single-line comment using '#'

"""
This is a 
multi-line comment
"""

# 2. Python Basics

"""
Integers (int)
Integers are numbers that do not have a decimal part.
In Python, they are represented simply by writing
the number without quotes or decimal points. For example:
"""

age = 20
quantity = 200

"""
Floats (float)
Floating-point numbers, also known as floats, are those that have a decimal part.
In Python, they are represented using a dot to separate the integer part from the decimal part. For example:
"""

price = 9.99
height = 1.85

"""
Strings
Strings are sequences of characters enclosed in 
single quotes ('...') or double quotes ("..."). 
They are used to represent text in Python. For example:
"""

name = "Arthur"
message = "Hello world"

print(f"{name}")

year = 2028

# 3. Control Structures

"""if year < 2023:
    print("The year is less than 2023")
elif year >= 2023 and year < 60:
    print("Year is greater than or equal to 2023 and less than 60")
elif year > 2025:
    print("The year is greater than 2025")
elif year == 2050:
    print("Year is equal to 2050")
else:
    print("The year is 2028")"""

# 3.1 LOOPS

# For

# fruit = "apple", "banana", "orange"

"""fruits = ["apple", "banana", "orange"]

for fruits in fruits:
    print(fruits)"""

# WHILE

"""counter = 0
while counter < 5:
    print(counter)
    counter += 1"""

# Some examples:

"""print("Numbers from 1 to 5 multiplied by 2 using 'for'")
for number in range(1, 6):
    print(number * 2)

print("Numbers from 1 to 5 multiplied by 2 using 'while'")
counter = 1
while counter <= 5:
    print(counter * 2)
    counter += 1"""

for i in range(10):
    if i % 2 == 0:
        print(i)