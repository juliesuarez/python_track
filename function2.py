def sum():
    num,num1 = 20,10
    num2 = num + num1
    print(num2)
sum()

#creating a dynamic function

def add(num,num1):
    num2 = num + num1
    print(num2)
add(40,10)

#modulus

def rem(num,num1): # the values are the parameters
    num2 = num % num1
    print(num2)
rem(100,90) # the values(real ones) are the arguements   

#subtraction

def sub(num,num1):
    num2 = num - num1
    print(num2)
sub(80,90) 

#divison

def div(num,num1):
    num2 = num/num1
    print(num2)
div(20,3)

#product

def prod(num,num1):
    num2 = num * num1
    print(num2) 
prod(2,5)

# a function is self contained ie sub can't do prod till required
# functions are indepedent of each other
# they must be first instructed to do so
