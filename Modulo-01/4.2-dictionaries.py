#Dictionaries[print]

"""
A dictionary is a mutable and unordered data 
structure that allows you to store key-value pairs. 
Each element in a dictionary consists of a unique 
key and its corresponding value. Dictionaries are 
delimited by curly braces {}, and key-value pairs 
are separated by commas.
"""

"""
Creation and Access
To create a dictionary, use curly braces and 
separate the keys and values ​​with a colon.
"""


"""
person = {"name": "John", "age": 25, "city": "Madrid"}

print(person["name"]) # print(person.get("name")) // print "jhon" 
print(person["age"]) # print 25
print(person["city"]) # print Madrid

"""



#Dictionar Methods

"""
Dictionaries in Python have several built-in methods for manipulating 
and accessing elements. Some common methods are:

keys(): returns a view of all the keys in the dictionary.

values(): returns a view of all the values ​​in the dictionary.

items(): returns a view of all the key-value pairs in the dictionary.

update(another_dictionary): updates the dictionary with the key-value pairs from another dictionary.
"""

person = {"name": "jhon", "age": 25, "city": "Madrid"}

print(person.keys()) # Prints dict_keys(["name", "age", "city"])
print(person.values()) # Prints dict_values(["John", 25, "Madrid"])
print(person.items()) # Prints dict_items([("name", "John"), ("age", 25), ("city", "Madrid")])

person.update({"profissao": "Engenheiro"})

print(person) # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}







