print('hello world')
age = 20
print(age)
price = 19.87
name = 'juliet smith'
print(name)
age = 20
print(age)
status = 'new patient'
print(status)
name =input('what is your name? ')
print('hello ' + name)
 
birth_year = int(input('enter your birth year: '))
age = 2023 - birth_year
print(age)
num = 1000
num2 = 99.45
print(num - num2)
first = float(input('first: '))
second = float(input('second: '))
sum = first + second
print('sum: ' + str(sum))
course = 'python for beginners'
print(course.upper())
print(course.find('y'))
print(course.find('n'))
print(course.find('b'))
print(course.replace('beginners', 'Ground for breakers'))
print('python' in course)
print(90//4)
x = 4
x += 3
print(x)
#comparison operators ie >,<,<=,>=,==,!=
 #logical operators ie and(both true),or(at least one is true),not

def temp():
    temperature = 35
    if temperature >= 35:
        print('its a hot day')
        print('Take some water')
    elif temperature <=35:
        print('weather is favorable')
        print('its a clear day')
temp()

weight = float(input('weight here: '))
unit = input("Kg or Lbs: ")
if weight == 'Kg':
    converted = weight/0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight*0.45
    print("weight in Kg: "+ str(converted))

i = 1
while i <= 10:
  i+=1  
  print(i * '*')

names = ['monica','juliet','van','trinity']
print(names[0:3])
print(names.append('Uganda'))
print(len(names))
print(names)

def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome please')
greet('Juliet', 'Nakawesi')