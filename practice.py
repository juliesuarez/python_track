#variables

#loops
#type casting
#coverting from one datatype to another
#concatenation refers to merging of strings together
'''
you can not merge a string and integer or float
the integer or float must be converted to string by str()
'''
name = 'Denis: '
age = 18
print(name + str(age))


'''
ASSIGNMENT
imagine there is a school,a nessary school antie esther that will help them store information of pupils,
 you required to input the interactive program with atleast one function 
things captured from students,name,DOB,name of the parent,class,location,state of payement(y/n)
should giv out the sammary of registered student
amount of money the student have to pay
The captured values should be appended in the list
push the work to the github
assignment of yesterday pushed 
'''































age =input('age: ')
print(type(age))
x=str(age)
print(type(x))
age =input('age: ')










print(type(name))
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
print('your age: ',age)
age()