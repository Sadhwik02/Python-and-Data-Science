#DataStructures
#1. Lists
fruits = ['apple', 'banana', 'cherry']
empty_list = []
print(len(fruits))  # Length of the list
print(fruits[0])  # Accessing first element
print(fruits[-1])  # Accessing last element
fruits.append('orange')  # Adding an element
print(fruits)
fruits.insert(1, 'kiwi')  # Inserting at index 1
print(fruits)
fruits.remove('banana')  # Removing an element
print(fruits)
print(fruits.pop())  # Removing and returning the last element
print(fruits)
fruits.sort()  # Sorting the list
print(fruits)
list2 = ['grape', 'kiwi']
fruits.append(list2)  # Appending another list
print(fruits)
list3 = fruits + list2  # Concatenating lists
print(list3)
list4 = fruits * 2  # Repeating the list
print(list4)
list5 = [1, 2, 3, 4, 5]
fruits.extend(list5)  # Extending the list with another list
print(fruits)
numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
# Slicing the list
print(numbers[2:5])  # Elements from index 2 to 4 Excludes 5
print(numbers[:5])  # First 5 elements
print(numbers[5:])  # Elements from index 5 to end
print(numbers[-5:])  # Last 5 elements
print(numbers[::2])  # Every second element
print(numbers[::-1])  # Reversed list
#Looping
for fruit in fruits:
    print(fruit)  # Iterating through the list
# List Comprehensions
squares = [x**2 for x in range(10)]  # Squares of numbers from 0 to 9
print(squares)
list_of_tuples = [(x, x**2) for x in range(5)]  # Tuples of number and its square
print(list_of_tuples)
list_of_strings = [str(x) for x in range(5)]  # Converting numbers to strings
print(list_of_strings)
# Memory Management
import sys
print(sys.getsizeof(fruits))  # Size of the list in bytes
# Copying Lists
list_copy = fruits.copy()  # Shallow copy of the list
print(list_copy)
#Split
s1 = "apple,banana,cherry"
s1_list = s1.split(',')  # Splitting string into list
print(s1_list)
# Join
s1_joined = ','.join(s1_list)  # Joining list into string
print(type(s1_joined))
print(s1_joined)
#Example
#Transpose of a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trans = []
for i in range(len(matrix[0])):
    lst = []
    for row in matrix:
        lst.append(row[i])
    trans.append(lst)
print(trans)
#Transpose using List Comprehension
transpose = [[row[i] for row in matrix] for i in range((len(matrix[0])))]
print(transpose)
# Frequency Count
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
from collections import Counter
frequency = Counter(numbers)  # Counting frequency of elements
print(frequency)
#or 
print(numbers.count(2))  # Counting occurrences of 2
unsorted_list = [5, 3, 1, 4, 2]
# Sorting the list
sorted_list = sorted(unsorted_list)  # Returns a new sorted list
reversed_list = sorted(unsorted_list, reverse=True)  # Returns a new sorted list in reverse order
print(sorted_list)
print(reversed_list)
# Sorting in place
unsorted_list.sort()  # Sorts the list in place
print(unsorted_list)
