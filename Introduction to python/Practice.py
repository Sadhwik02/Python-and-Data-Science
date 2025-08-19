#Write a function that inputs a number and prints the multiplication table of that number
num = int(input("Enter a number:"))
def mul_table(num):
    for i  in range(1,11):
        print(f"{num} x {i} = {num*i}")
mul_table(num)
# Write a program to print twin primes less than 1000. If two consecutive odd numbers are both prime then they are known as twin primes
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0 :
            return False
    return True   
def twin_primes():
    for i in range(3,1000,2):
        if is_prime(i) and is_prime(i+2):
            print(f"{i} {i+2} are twin primes")
twin_primes()
# Write a program to find out the prime factors of a number. Example: prime factors of 56 - 2, 2, 2, 7
def prime_factors(n):
    factors = []
    for i in range(2,n+1):
        while n%i==0:
            factors.append(i)
            n//=i
    return factors
num = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(num)
print(f"Prime factors of {num} are: {factors}")
# Write a program to implement these formulae of permutations and combinations. 
# Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!. Number of 
# combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else: return n*fact(n-1)
def permutations(n,r):
    return fact(n)//fact(n-r)
def combinations(n,r):
    return permutations(n,r)//fact(r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"Permutations of {n} objects taken {r} at a time: {permutations(n,r)}")
print(f"Combinations of {n} objects taken {r} at a time: {combinations(n,r)}")
# Write a function that converts a decimal number to binary number
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n>0:
        binary = str(n%2) + binary
        n //= 2
    return binary

num = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(num)
print(f"Binary representation of {num} is: {binary_representation}")
# Write a function cubesum() that accepts an integer and returns the sum of the cubes of 
# individual digits of that number. Use this function to make functions PrintArmstrong() and 
# isArmstrong() to print Armstrong numbers and to find whether is an Armstrong number
def cubesum(n):
    sum_cubes = 0
    while n>0:
        digit = n%10
        sum_cubes+=digit**3
    return sum_cubes
def isArmstrong(n):
    return n == cubesum(n)
def PrintArmstrong(limit):
    print(f"Armstrong numbers up to {limit}:")
    for i in range(limit + 1):
        if isArmstrong(i):
            print(i, end=" ")
limit = int(input("Enter a limit to find Armstrong numbers: "))
PrintArmstrong(limit)

