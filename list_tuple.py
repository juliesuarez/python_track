#list,tuple and dictionary(dict) in details!
#lists are muteable datatypes(can be deleted,)!
'''
 mult line comment!
'''
def my_list():
    #declaring my list!
    this_list = [0,1,2,3,4,5,6,7,8,9]
    print (this_list[1])
my_list()

'''
Mult line comment(can be written above the function)!
'''

def my_list2():
    #Declaring my list(can be written with in a defined function)!
    this_list2 =[10,20,30,40,50]
    print (this_list2 [4])
    print (this_list2 [-1])
my_list2()    
    

def osman():
    #Declaring in osman!
    osman = [100,[200]]
    print(osman[1][0])
osman()

def osman2():
    #Declaring in osman2!
    osman2 = [1000,[[2000,3000]]]
    print(osman2[1][0][1])
osman2()    


#tuples
#immutable(you can  not delete anything in a tuple).

'''
Mult line comments
'''
def my_tuple():
    #Declaring my_tuple!
    my_tuple = (10,20,30,40,50)
    print(4)
my_tuple()


def osman():
    #Examples of muteable lists!
    osman.append(1000)
    print(osman)
    osman.pop()
    print(osman)
osman()

def my_fruits():
    #Declaring my fruits!
    fruits =["orange",'pineapple']
    fruits.append("apple")
    print(fruits)
    fruits.pop()
    print('fruits')
    fruits.remove("orange")
    print(fruits)
my_fruits()    

def mapping():
    #Mapping in details(dictionary(dict)
    # Dict is muteable,you can delete or add 
    zebra = {'name':'tongs','legs':4,'color':'black & white','sex':'male'}
    print(zebra.keys ())
    print(zebra.values ())
    zebra.__delitem__('name')

mapping()

def my_tuple():
    #Declaring my_tuple
    tuple1 = ('realmardrid','spurs','vipers','kcc')
    print(0)
my_tuple()