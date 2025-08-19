#Sets
#Sets are unordered collections of unique elements.
#Sets have no duplicate elements and are mutable.
#Sets doesnt have indexing, slicing, or other sequence-like behavior.
# Creating a set
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Accessing elements (not by index, but by membership)
print(5 in numbers_set)  # Checking if an element is in the set
s = set() # Creating an empty set
# Adding elements to the set
s.add(11)
s.add(12)
s.add(13)
print(s)  # Printing the set after adding elements
s.update([14, 15])  # Adding multiple elements
print(s)
s.update([10, 16])  # Adding elements from another set
print(s)
# Removing elements from the set
s.remove(11)  # Removing an element (raises KeyError if not found)
print(s)
s.discard(12)  # Removing an element (does not raise error if not found)
print(s)
s.pop()  # Removing and returning an arbitrary element
print(s)
s.pop()  # Removing another arbitrary element
print(s)
# Clearing the set
s.clear()  # Removing all elements from the set
print(s)  # Printing the empty set
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union of two sets
print(set1.union(set2))  # Printing the union of set1 and set2
# Intersection of two sets
print(set1.intersection(set2))  # Printing the intersection of set1 and set2
# Difference of two sets
print(set1.difference(set2))  # Printing the difference of set1 and set2
# Symmetric difference of two sets
print(set1.symmetric_difference(set2))  # Printing the symmetric difference of set1 and set2
# Copying sets
set_copy = set1.copy()  # Shallow copy of the set
print(set_copy)  # Printing the copied set
print(set1.issubset(set2))  # Returns False, as set1 is
# Set Comprehensions
# Set comprehensions are a concise way to create sets.
# They consist of an expression followed by a for clause, then zero or more for or if clauses
# Creating a set of squares of numbers from 1 to 10
squares_set = {x**2 for x in range(1, 11)}
print(squares_set)  # Printing the set of squares
# Example of set comprehension with condition
# Creating a set of even numbers from 1 to 10
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)  # Printing the set of even numbers
# Example of set comprehension with multiple conditions
# Creating a set of numbers from 1 to 10 that are both even and greater than 5
even_and_greater_set = {x for x in range(1, 11) if x % 2 == 0 and x > 5}
print(even_and_greater_set)  # Printing the set of even numbers greater than 5
#Frozensets
# Frozensets are immutable sets, meaning they cannot be changed after creation.
# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Printing the frozenset
# Attempting to add an element to a frozenset will raise an error
try:
    frozen_set.add(6)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")
# Example of frozenset operations
frozen_set2 = frozenset([4, 5, 6, 7, 8])
# Union of frozensets
print(frozen_set.union(frozen_set2))  # Printing the union of two frozensets
# Intersection of frozensets
print(frozen_set.intersection(frozen_set2))  # Printing the intersection of two frozensets
# Difference of frozensets
print(frozen_set.difference(frozen_set2))  # Printing the difference of two fro




