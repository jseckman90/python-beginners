# Print
print('hello world')
print('*' * 10)

name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

user_weight = input('Weight in lbs? ')
lbs_to_kg = int(user_weight) * .453592
print(lbs_to_kg)