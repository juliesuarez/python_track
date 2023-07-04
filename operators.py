# Operators in python
# What are operators?
# An operator tells a computer what to do with an operand.
# What is an operand?
# An operand is a value acted upon by the operator. its what is assigned to the variable.
# Different categories of operators
# Arithmetic operators(+,-,/,//(floor division,rounds off to the nearest whole number),%(modulus,takes the remaider),**(means exponetial))
# Examples
num = 10
num1 = 20
print (num + num1)
print (num * num1)
print (num - num1)
print (num / num1)
print (num // num1)
print (num % num1 )
print (num ** num1)

# Assignment operators(=(assignment),+=,-=,*=,/=,%=,**=)

num3 = 50
num4 = 100
num3 += num4 #(num3 = num3 + num4)
print(num3)
num3 -= num4
print(num3)
num4 *= num3
print(num4)
num4 /= num3
print(num4)
num4 %= num3
print(num4)

# comparision operators(==,!=(not equal),<>,>=,<=)
print(num == num1)
print(num != num1)
print(num < num1)
print(num <= num1)
print(num >= num1)

# logical operators(and,or,not)
print(True and True)
print(True and False)
print(True or False)
print(not True)

#identity operators( is,is not)
name = "suarez"
print (num3 is num4)
print (num3 is not num4)

#membership operators(in, not in)
print ("a" in name)
print ("o" in name)
print ("A" in name)
print ("o" not in name)