
def payee(salary,name,location,age,type_of_work):
    rate = 0.3
    if salary >= 300000:
      tax = rate * salary
      net_pay = salary - tax
      print('***********************')
      print('Dear: ',name)
      print('Your tax payeable is: ',tax)
      print('And your final salary is: ',net_pay)
      print('.............................')
    else:
       print("Dear: ",name)
       print('Your salary is non-taxable')   


print('Welcome our dear customer! ')
name = raw_input('please Ener name here:  ')
location = raw_input('Please Enter your location: ')
age = int(input('Please Enter your year of birth: '))
type_of_work = raw_input('Please Enter the kind of work: ')
salary =input('please Enter salary here: ')

print(type(salary))

payee(salary,name,location,age,type_of_work)