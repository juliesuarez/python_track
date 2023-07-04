#variables
name = 'julie'
print(name)

name = 'suarez'
age = 20
height_in_cm = 100.0
weight_in_kg = 60
print(name,height_in_cm,weight_in_kg)

first_name = 'julie'
last_name = 'suarez'
print(first_name + last_name )

my_text = 'I love Nalugya Vanessa to'
number = 100
print(my_text + str(100))


Dorm = 'Mpaga'
name1 = 'Julie'
name2 = 'Vanesa'
name3 = 'Angel'
name4 = 'Trinity'
#print(f'The Mpaga called{Dorm} has girls like{name1},{name2},{name3} and {name4}' )

#input



#dictionaries
capitals = {'uganda':'kampala','kenya':'nairobi','tanzania':'dodoma'}
print(capitals.keys())
print(capitals.values())
print(capitals.get('uganda'))
print(capitals.pop('kenya'))
print(capitals.popitem())

def age():
   date_of_today = int(input('Please Enter the date of today: '))
   date_of_birth = int(input('Please Enter the birth year: '))
   age = date_of_today - date_of_birth

age()