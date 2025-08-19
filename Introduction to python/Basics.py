import keyword
print(keyword.kwlist)#Prints the keywords
print(len(keyword.kwlist))#There are 35 keywords
a=3
b=3
print(id(a))
print(id(b))#Both variables have same location because the value is same
#DataTypes
#1. Integers
print(type(10))#Integer
#2. Float
print(type(10.5))#Float
#3. Complex
print(type(10+5j))#Complex
#4. Boolean
print(type(True))#Boolean
#5. String
print(type("Hello"))#String '' or ""
#6. List
print(type([1,2,3]))#List   Mutable
#7. Tuple
print(type((1,2,3)))#Tuple  Immutable
#8. Dictionary
print(type({"name":"John"}))#Dictionary   Key,value pairs values are accessed using keys
#9. Set
print(type({1,2,3}))#Set   unique elements
#10. Frozen Set
print(type(frozenset({1,2,3})))#Frozen Set  immutable set


#Output formatting
c=10
d=20
print("First number :{} Second number :{}".format(c,d))
print("Second number :{1} First number :{0} ".format(c,d))
print("Hello {name}".format(name="nani"))
#Input
#name=input("Enter your name:")
#print(name)


#Operators
#1. Arithmetic Operators + - * / // % **
#2. Comparision > < >= <= != ==
#3. Logical Operators and or not
#4. Assignment Operators = += -= *= /= %= **= //= <<= >>= &= ^= |=
#5. Membership Operators in not in (in dicts only checks keys)
d={1:"a",2:"b",3:"c"}
print(1 in d) #True
print(2 in d) #True
print(4 not in d) #True
#6. Identity Operators is not is (checks memory location)
l1=[1,2,3,4]
l2=[1,2,3,4]
print(l1 is l2)#False
s="asd"
s2="asd"
print(s is s2) #True
#7. Bitwise &  | ~ ^ >> <<


#IfElse
#1. if-else
age=20
if age>18:
    print("Adult")
else:
    print("not adult")
#2. Nested if else
age=20
if age>18:
    print("Adult")
    if age>30:
        print("Uncle")
    else:
        print("Young")
else:
    print("not adult")

#Loops
#1. For Loop
#2. While Loop
#3. Nested Loops
#4. Loop Control Statements break continue pass
#5. Enumerate
#6. Zip
#7. Itertools
#8. Generators
#9. Lambda Functions
#10. Map Filter Reduce
#11. Set
#12. Dictionary
#13. Tuple
#14. List
#15. String
#16. Array
#17. Matrix
#18. Dictionary Comprehension
#19. List Comprehension
#20. Set Comprehension
#21. Context Manager

