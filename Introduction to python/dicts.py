#Dictionaries
# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  # Printing the dictionary
# Accessing values
print(my_dict["name"])  # Accessing value by key
print(my_dict.get("age"))  # Using get method to access value
my_dict["name"] = "nani"
print(my_dict)  # Updating value
my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)  # Printing the updated dictionary
my_dict.pop("age")  # Removing a key-value pair
print(my_dict)  # Printing the dictionary after removal
my_dict.popitem()# Removing a key-value pair using popitem
print(my_dict)  # Printing the dictionary after removal
del my_dict["city"]  # Deleting a key-value pair
print(my_dict)  # Printing the dictionary after deletion
my_dict.clear()  # Clearing the dictionary
print(my_dict)  # Printing the empty dictionary
subjects = {}.fromkeys(['math', 'science', 'history'], 0)  # Creating a dictionary with default values
print(subjects)  # Printing the dictionary with default values
print(subjects.items())  # Getting items of the dictionary
print(subjects.keys())  # Getting keys of the dictionary
print(subjects.values())  # Getting values of the dictionary
# Looping through a dictionary
d = {"a": 1, "b": 2, "c": 3}
for pair in d.items():
    print(pair)  # Printing key-value pairs
for key,val in d.items():
    print(f"key: {key}, value: {val}")
# Dictionary Comprehensions
# Creating a dictionary using dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}  # Squaring numbers from 0 to 4
print(squared_dict)  # Printing the dictionary of squares
