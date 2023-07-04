# numeric datatype,string,sequence,mapping,boolean,set,
# numerics (integers(int),float,complex)

num1 = 1000
#int
num2 = 1000.0
#float
num3 = 1 + 2j
#complex
print (type (num1))
print (type (num2))
print (type (num3))

# string(str)(any value in single or double quotes is a string)
num4 = "1000"
name = "julie"
print (type (num4))
print (type (name))

#sequence(lists,tuple,range)
my_list = [0,2,4,6]
my_list2 = [0,2,4,6,"julie",10.5] 
my_tuple = (0,2,4,6)
print (type (my_list))
print (type (my_list2))
print (type (my_tuple))

#mapping (dict(dictionary))
my_dict = {"uganda" : "kampala", "italy" : "rome","france" : "pari","tanzania" : "dodoma" }
print (type (my_dict))

# boolean(True or False)

#Set
my_set = {0,5,15,20}
my_set2 = {0,0,5,5,15,15,20,20}
print (my_set)
print (my_set2)
print (set (my_dict))
