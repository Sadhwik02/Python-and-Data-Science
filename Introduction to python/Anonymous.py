#Anonymous functions
double = lambda x: x*2
print(double(5))  # Output: 10
#Filter
lst = [1, 2, 3, 4, 5]
even_lst = list(filter(lambda x: x%2==0,lst))
print(even_lst)  # Output: [2, 4]
#Map
lst_2 = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, lst_2))
print(squared_list)  # Output: [1, 4, 9, 16, 25]
from functools import reduce
lst_3 = [1, 2, 3, 4, 5]
prod = reduce(lambda x,y: x*y, lst_3)
print(prod)  # Output: 120