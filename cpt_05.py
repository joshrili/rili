'''
Description: python code, exercises of chapter 5, python crash course

Author: joshrili
Date: 2020-03-22

'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
for car in cars :
    if car == 'bmw' :
        print(car.upper())
        print('I like ' + car.upper() + '\n')
    else :
        print(car.title())
        print('I like ' + car.title() + '\n')
print('I like all these cars above!')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

alien_colors = ['green' , 'yellow' , 'red']
for alien_color in alien_colors :
    if alien_color == 'green' :
#if alien_color == 'red':
        print('Great! You have shotted a green alien, and earned 5 points.')
    elif alien_color == 'yellow' :
        print('Great! You have shotted a yellow alien, and earned 10 points.')
    elif alien_color == 'red' :
        print('Great! You have shotted a red alien, and earned 15 points.')

usernames = ['Admin' , 'chen' , 'li' , 'hu']
#usernames = []
if usernames :
    for user in usernames :
        if user == 'Admin' :
            print('Hello Admin, see a report?')
        else:
            print('Hello ' + user + ', thank for logging.')
else:
    print('we need some users.')

del usernames[:]
#del usernames #delete the elements and the list
print(usernames)
if usernames :
    print('Not empty')
else :
    print('empty')

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
