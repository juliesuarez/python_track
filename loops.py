# loop is an instruction that will tell the computer to repeatedly perform specific task

def my_count():
    for number in range(10):
        print(number)
my_count()
# for is a key word for loop
#number can be anything,it reprsents a value at a particular point

#access list elements using a loop
def example2():
    languages = ['python', 'javascript','Ruby','c++','nodejs']
    for language  in languages:
        print(language)
example2()

def example3(num):
    for number in range(num):
        print(number)
example3(5)
example3(8)

def my_lang():
     languages = ['python', 'javascript','Ruby','c++','nodejs']
     for language in languages:
         if language == 'python':
             print('your currently in python class')
my_lang()
#== compare

def even(num):
    for number in range(num):
        if number % 2 == 0:
           print(number)
even(10)
#change function even to printing odd numbers

def odd(num):
    for number in range(num):
        if number % 2 != 0:
           print(number)
odd(10)

def power(p):
    my_po = p**2
    if my_po % 2 == 0:
        print("The power is an even number")
    else:
        print('The power is an odd number')
power(6)