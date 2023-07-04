#How functions communicate to each other
# Dynamic functions or paramaterised functions
def add(num,num1):
    num2 = num + num1
    print(num2) 


def sub(num,num1):
    num2 = num - num1
    print(num2)  

# allowing functions to communicate

def add2(num1,num2): # num1 and num2 are called parameters
    num3 = num1 + num2
    print(num3) 
    return num3 + 10 # return stops the whole process stand(ends execution,gives the value we can need)

#the values we give when calling a function are called arguments or actual parameter or formal parameters
#like 5,7,10

add2(2,3)
ans = add2(100,50)
print(ans)
print(add2(2,3))

# function sub2 is a calling function of add2 
