
student = []
def my_students():
    print('Welcome our Dear student to Esther Nursery School!')
    fees = 5000000
    print('You pay: ',fees)
    name_of_student = input('Please Enter your name: ')
    current_year = int(input ('Please Enter current year: '))
    Year_of_birth = int(input('Please Enter birth year: '))
    age = current_year -Year_of_birth
    print('Your age is: ',age)
    location = input('Please Enter location: ')
    name_of_parent = input('Please Enter parent name: ')
    state_of_payment = input('Please enter the paid/unpaid: ')
    if state_of_payment == "paid":
        print('Dear :',name_of_student, 'YES')
    else:
        print('Dear : ',name_of_student, 'NO')     

    student_dict = {
        'Your name': name_of_student,
        'Parent': name_of_parent,
        'date_of_birth': Year_of_birth,
        'Place of residence':location,
        'Amount':fees,
        'paid/unpaid':state_of_payment,
    }
    
    student.append(student_dict)
    print(student)
my_students()

