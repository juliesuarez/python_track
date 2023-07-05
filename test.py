


def payee(salary,name,location,type_of_work):
    current_year = input('Please Enter current date: ')
    Year_of_birth = input('Please Enter birth year: ')
    age = current_year - Year_of_birth
    print('your age is: ',age)
    rate = 0.3
    if salary >= 300000:
      tax = rate * salary
      net_pay = salary - tax
      print('***********************')
      print('Dear: ',name,salary,age,location,type_of_work)
      print('Your tax payeable is: ',tax)
      print('And your final salary is: ',net_pay)
      print('.............................')
      print('Thank you!')
    else:
       print("Dear: ",name)
       print('Your salary is non-taxable')   


print('Welcome our dear customer! ')
name = raw_input('please Ener name here:  ')
location = raw_input('Please Enter your location: ')
#current_year = input('Please Enter current year: ')
#Year_of_birth = input('Please Enter your year of birth: ')
type_of_work = raw_input('Please Enter the kind of work: ')
salary =input('please Enter salary here: ')

print(type(salary))

payee(salary,name,location,type_of_work)

