#tuples
#tuples are immutable sequences in Python, used to store multiple items in a single variable.
# Creating a tuple
num = (1,2,3,4,5,6,7,8,9,10)
# Accessing elements
print(num[0])  # Accessing first element
print(num[-1])  # Accessing last element
# Length of the tuple
print(len(num))  # Length of the tuple
# Slicing the tuple
print(num[0:5])  # Slicing the tuple from index 0 to 5
print(num[:5])  # First 5 elements
print(num[5:])  # Elements from index 5 to end
# Tuple meth ods
print(num.index(5))  # Finding index of an element
print(num.count(5))  # Counting occurrences of an element
# Looping through a tuple
for n in num:
    print(n)  # Iterating through the tuple
# Tuple unpacking allocates the value of the tuple to multiple variables
# Unpacking a tuple
a, b, c, d, e = num[:5]  # Unpacking first 5 elements
print(a, b, c, d, e)  # Printing unpacked values
# Converting a list to a tuple
fruits = ['apple', 'banana', 'cherry']
fruits_tuple = tuple(fruits)  # Converting list to tuple
print(fruits_tuple)  # Printing the tuple
# Tuple with a single element
single_element_tuple = (42,)  # Note the comma
print(single_element_tuple)  # Printing single element tuple
print(type(single_element_tuple))  # Checking type of single element tuple
print(type(fruits_tuple))  # Checking type of fruits tuple
# Memory Management
import sys
print(sys.getsizeof(num))  # Getting size of the tuple in bytes
# Copying Tuples
tuple_copy = num  # Tuples are immutable, so this is a reference copy
print(tuple_copy)  # Printing the copied tuple
# Example of a tuple with mixed data types
mixed_tuple = (1, 'apple', 3.14, True)  # Tuple with mixed data types
print(mixed_tuple)  # Printing mixed data type tuple
unsorted_tuple = (5, 3, 1, 4, 2)
# Sorting the tuple
print(sorted(unsorted_tuple))  # Returns a new sorted list from the tuple
print(sorted(unsorted_tuple, reverse=True))  # Returns a new sorted list in reverse order
# Sorting in place is not applicable for tuples as they are immutable
print(max(num))  # Maximum value in the tuple
print(min(num))  # Minimum value in the tuple
print(sum(num))  # Sum of all elements in the tuple
# Example of a tuple of tuples
tuple_of_tuples = ((1, 2), (3, 4), (5, 6))  # Tuple containing other tuples
print(tuple_of_tuples)  # Printing tuple of tuples
#Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple_concatenated = tuple1 + tuple2  # Concatenating two tuples
print(tuple_concatenated)  # Printing concatenated tuple

