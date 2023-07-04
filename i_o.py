'''
def payee():
    name  = input('please enter your name: ')
    salary = int(input('please enter your salary: '))
row_input was designated to capture strings
input was designated to captures integers and numerics
'''
# predefined and user functions are types of functions.
#prefined function like print,input(captures values from the keybord)
#in py2 they had two functions to capture values in the keybord
#either use input and row input
#in py3 they discarded the row input
# in python 2 print was just a statement not a function
#write python space and wite something in quotes.
#input func is used to capture values from the keybord
# however captures everything from a keybord as a string by default
#in py3 input function expects everything to be a string

# calculating payee
def payee(salary,name):
    rate = 0.3
    tax = rate * salary
    net_pay = salary - tax
    print('***********************')
    print('Dear: ',name)
    print('Your tax payeable is: ',tax)
    print('And your final salary is: ',net_pay)
    print('.............................')
    


print('Welcome our dear customer! ')
name = raw_input('please Ener name here:  ')
salary =input('please Enter salary here: ')

print(type(salary))

payee(salary,name)