
'''
 Below are properties/attributes of  a defined class girl 
 all objects under this class must fulfill these attributes
 ASSIGNMENT; create at least 10 classes with corresponding five objects
 five printing for each
 all objects in the same class have the same method
 we have static and dynamic classes
'''

class Girl:#static class
    name ='Juliet' 
    age = 20
    gender = 'Female'
    size  = 'Chubby'
    family = "Mulagira Family"
    size_of_bra = 'Small'
    def dance(): # this is a method
        return 'She likes Kalipuso'
    def bathe():
        print('Two times a day') # this is a behaviour
    def greet():
        print('Hey World')
        print('Hello World! ')
        return ''
print(Girl.greet())
Girl.bathe() #line 26 prints out a property
Girl.dance()
print(Girl.dance())  #you must call it to print the return statement,# line 28 is printing out a method dance
print(Girl.name)
print(f"{Girl.name} is {Girl.age} years old and {Girl.size} {Girl.gender} from {Girl.family}")

girl2 = Girl()
girl2.name = 'Vanessa'
girl2.age = 16
girl2.gender = 'Female'
print(girl2.name)
print(f"{girl2.name} is {girl2.age} years old")

girl3 = Girl()
girl3.name = 'Trinity'
girl3.age = 10

