# # Print
# print('hello world')
# print('*' * 10)

# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' likes ' + color)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print(age)

# user_weight = input('Weight in lbs? ')
# lbs_to_kg = int(user_weight) * .453592
# print(lbs_to_kg)



# string = '100 Days of Code'

# print(string)
# print(string[0])
# print(string[0:4])
# print(string[-1])
# print(string[1:-1])
# print(string[:])


###################
# Formatted Strings
###################

# first_name = "Josh"
# last_name = "Seckman"

# message = first_name + ' [' + last_name + '] is a coder'
# msg = f'{first_name} [{last_name}] is a coder'
# print(message)
# print(msg)


###################
# String Methods
###################
challenge = '100 Days of Code'

# Len - returns number of characters including spaces
print(len(challenge))

# Upper - creates a new string and returns it capitalized
print(challenge.upper())

# Lower - creates a new string and returns it lowercased
print(challenge.lower())

# Find - find index of what is passed in.  Case sensitive
print(challenge.find('Days'))

# Replace - replace a character or sequence of characters.  first argument is what you want to replace, and the second argument is what is replacing the first argument.  Case sensitive
print(challenge.replace('Days', 'Years'))

# in operator - check to see if the string contains a character or sequence of characters. returns boolean. case sensitive
print('Days' in challenge)
output = 16
output = 100 DAYS OF CODE
output = 100 days of code
output = 4
output = 100 Years of Code
output = True

