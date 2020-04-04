'''
Description: python code, exercises of chapter 4, python crash course

Author: joshrili
Date: 2020-03-21

'''
pizzas = ['pepperoni' , 'bacon' , 'beef']
for pizza in pizzas :
    print('I like ' + pizza + ' pizza.')
print('I really like pizza!')

numbers = list(range(1 , 11))
print(numbers)

squares = []
for val in range(1 , 11) :
    squares.append(val ** 2)
print(squares)

# list comprehension
squares = [val ** 2 for val in range(1 , 11)]
cubes = [val ** 3 for val in range(1 , 11)]
print(squares)
print(cubes)
print(max(squares))
print(min(squares))
print(sum(squares))
print(len(squares))

num_list = [val for val in range(0 , 1000000)]
print(sum(num_list))
print(num_list[-3 : -1]) #up to the last but not include
print(num_list[-1]) #the last element


#tuple
dimension = tuple()
dimensions = (200 , 30)
for dem in dimensions :
    print(dem)
print(dimension)   #()
print(dimensions[0])
#dimensions[0] = 1000 #error, do not support item assigment
dimensions = (1000 , 300)  #write over a exist tuple is legal
print(dimensions)
    
