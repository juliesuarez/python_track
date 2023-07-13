# numeric datatype,string,sequence,mapping,boolean,set,
# numerics (integers(int),float,complex)

NUM1 = 1000
#int
NUM2 = 1000.0
#float
NUM3 = 1 + 2j
#complex
print (type (NUM1))
print (type (NUM2))
print (type (NUM3))

# string(str)(any value in single or double quotes is a string)
NUM4 = "1000"
NAME = "julie"
print (type (NUM4))
print (type (NAME))

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
