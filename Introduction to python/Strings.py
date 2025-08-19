#Strings
s = "Hello, World!"
st = 'This is a string'
s2 = """This is a
multiline string
that spans multiple lines."""
s3 = '''This is also a  multiline string
that spans multiple lines.'''
print(s+st)
print(s*3)
print(s[0])  # Accessing the first character
print(s[1:5])  # Slicing the string from index 1 to 4
print(s[-1])  # Accessing the last character
print(s[7:])  # Slicing from index 7 to the end
print(s[:5])  # Slicing from the start to index 4
print(s[::2])  # Slicing with a step of 2
print(s[::-1])  # Reversing the string
print(s.upper())  # Converting to uppercase
print(s.lower())  # Converting to lowercase
print(s.title())  # Converting to title case
print(s.capitalize())  # Capitalizing the first letter
print(s.strip())  # Removing leading and trailing whitespace
print(s.replace("World", "Python"))  # Replacing a substring
print(s.split(","))  # Splitting the string by comma
print(s.split())  # Splitting the string by whitespace
print(s.find("World"))  # Finding the index of a substring
print(s.index("World"))  # Finding the index of a substring (raises error if not found)
print(s.count("l"))  # Counting occurrences of a character
print(s.startswith("Hello"))  # Checking if the string starts with a substring
print(s.endswith("!"))  # Checking if the string ends with a substring
print(s.isalpha())  # Checking if the string contains only alphabetic characters
print(s.isdigit())  # Checking if the string contains only digits
print(s.isalnum())  # Checking if the string contains only alphanumeric characters
#Strins are immutable
# Attempting to modify a string will raise an error
try:
    s[0] = 'h'  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")
#looping through a string
for char in s:
    print(char)  # Printing each character in the string
# String Comprehensions
# Creating a new string with uppercase letters
uppercase_string = ''.join([char.upper() for char in s if char.isalpha()])
print(uppercase_string)  # Printing the new string with uppercase letters
# String Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
#Palindrome Check
string_to_check = "radar"
def is_palindrome(s):
    return s==s[::-1]
print(f"Is '{string_to_check}' a palindrome? {is_palindrome(string_to_check)}")

