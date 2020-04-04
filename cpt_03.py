'''
Description: python code, exercises of chapter 3, python crash course

Author: joshrili
Date: 2020-03-21

'''
friends = ['josh' , 'lichenshuo' , 'chenjie']
for friend in friends :
    print(friend)
print('Hello, ' + friends[0].title())
print('Hello, ' + friends[1].title())
print('Hello, ' + friends[2].title())

transports = ['car' , 'bycicle' , 'motor' , 'honda']
print('I would like to own a ' + transports[-1].title() + ' motorcycle.')

guests = ['josh' , 'lichenshuo' , 'chenjie']
print(guests[0].title() + ', Would you like to have dinner with me?')
print(guests[1].title() + 'can not have dinner with me.')

guests[1] = 'chenchen'
print(guests[1].title() + ', Would you like to have dinner with me?')

guests.insert(0 , 'rili')
guests.append('hu')
guests.insert(3 , 'chen')
print(guests)
guests.insert(-1 , 'mama')
print(guests)
del guests[0]
del guests[:1]
print(guests)
removed_name_is_none = guests.remove('chen')
print(removed_name_is_none) #None
print(guests)
popped_name = guests.pop(0)
print(popped_name)
print(guests)

#two ways to copy a list
new_guests = guests
print(new_guests)
new_guests.insert(1 , 'zhou')
print(guests)
print(new_guests)  #new_guests and guests have the same elements

another_guests = guests[:]
another_guests.insert(0 , 'rili')
print(another_guests)
print(guests)

print(guests.sort()) #None
print(guests) #the guests list has been sorted

print(sorted(another_guests , reverse = True))
print(another_guests) #the original list have not been sorted

print(another_guests.reverse()) #None
print(another_guests)
print(len(another_guests))
