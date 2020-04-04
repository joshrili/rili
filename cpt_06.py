'''
Description: python code, dictionary exercises of chapter 6, python crash
Author: joshrili
Date: 2020-03-22

'''
alien_0 = {'color' : 'green' , 'point' : 5}
alien_0['X_position'] = 0
alien_0['Y_position'] = 25
print(alien_0)
alien_0['color'] = 'red'
print(alien_0)
alien_0['speed'] = 'medium'
alien_0['to_del'] = 1
print(alien_0)
del alien_0['to_del']
print(alien_0)

person_informations = {}
person_informations['first_name'] = 'josh'
person_informations['last_name'] = 'rili'
person_informations['age'] = 35
person_informations['city'] = 'beijing'
print(person_informations)

favorite_numbers = {
    'josh' : 16,
    'chenchen' : 12,
    'jie' : 25,
    }
print(favorite_numbers)
print(favorite_numbers.items())

for name , num in favorite_numbers.items() :
    print(name + "'s favorite number is " + str(num))

for name in sorted(favorite_numbers.keys()) :
    print(name.title())

for name in favorite_numbers :
    print(name)

for num in favorite_numbers.values() :
    print(num)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()) :
    print(name.title())

for value in set(favorite_languages.values()) : #delete the duplicated element
    print(value)

aliens = []
for alien_number in range(30) :
    new_alien = {'color' : 'green' , 'point' : 5 , 'speed' : 'slow'}
    aliens.append(new_alien)
    print(new_alien)
#print(aliens)
print(len(aliens))

for alien in aliens[:15] :
    if alien['color'] == 'green' :
        alien['speed'] = 'medium'
        alien['color'] = 'yellow'
        alien['point'] = 10
        print(alien)

for alien in aliens[:5] :
    if alien['color'] == 'yellow' :
        alien['speed'] = 'fast'
        alien['color'] = 'red'
        alien['point'] = 15
        print(alien)

print(len(aliens))

favorite_languages = {
    'jen' : ['python' , 'ruby'] ,
    'sarah' : ['C'] ,
    'edward' : ['ruby' , 'go'] ,
    'phil' : ['python' , 'haskell'] ,
    'josh' : ['python' , 'java'] ,
    'jie' : ['C#' , 'sql'] ,
    }
for key in favorite_languages.keys() :
    print('\n' + key + "'s favorite language are:")
    for lang in favorite_languages[key] :
        print(lang)
for name , languages in favorite_languages.items() :
    print('\n' + name + "'s favorite languages are: ")
    for language in languages :
        print('\t' + language)

users = {
    'rili' : {
        'first' : 'josh' ,
        'last' : 'rili' ,
        'location' : 'beijing' ,
        } ,
    'chen' :{
        'first' : 'jie' ,
        'last' : 'chen' ,
        'location' : 'beijing' ,
        }
    }

for username , user_info in users.items() :
    print('Username is ' + username)
    print('Full name is ' + user_info['first'].title() + ' ' + user_info['last'].title())
    print('Location is ' + user_info['location'].title())
