'''
Description: python code, exercises of chapter 2, python crash course

Author: joshrili
Date: 2020-03-21

'''


#print('hello, python crash course')
#exercises about the string type
person_name = 'josh'
print('Hello ' + person_name + ', would you like to learn some Python today?')
print(person_name.lower())
print(person_name.upper())
print(person_name.title())
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
person_famous = 'Albert Einstein'
message = person_famous + ' once said, "A person who never made a mistake never tried anything new."'
print(message)
person_name = '\tjoshrli \t'
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())


#exercises about the integer and float types
print(2 + 6)
print(9 - 1)
print(2 * 4)
print(int(16 / 2))
print(2 ** 3)
print(17 // 2)
print(17 % 9)

favorite_num = 7
print('my favorite number is ' + str(favorite_num))
