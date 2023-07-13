'''
the method of a class __init__(constructor)will help us give the actual values of the object
constructor is used to initialize an instantiated object
constructor acts as a bridge for paremeters and arguments( real values of the object)
these values are assigned to to the properties of the class ie name,motto
self is a reference that denotes the properties/attributes of the class
'self' is an identifier to the properties of the specific object.
"self" is alterable/changeable ie self can be anything
"self" is a sometimes refered to as a sheshe for the method __init__
self.name is a property
the values of the method will be arguments for the class.
intantiation is actual creation of objects in the class.
it also involves giving the class their real properties/features.
the method register is overloaded coz each object uses it differently.   
'''
class School:# dynamic class
    def __init__(self,name,motto,location,nu_teachers,nu_admins,nu_stud,uneb_no):
        self.name = name 
        self.motto = motto
        self.location = location
        self.nu_teachers = nu_teachers
        self.nu_admins = nu_admins
        self.nu_stud = nu_stud
        self.uneb_no = uneb_no 
    def register(self):
        print(f"{self.name} is fully registered with UNEB.")

school1 = School('HKMC', 'In God we trust','Wakiso',40,10,2000,'U1076') # calling the class is called instantiation
school1.register()
school2 = School('Refactory','Improving Tech in Uganda', 'Muyenga',10,2,35,'U1024')
school2.register()
class Country:
    def __init__(self,A,B,C):
        self.name = A
        self.city = B
        self.pop =  C
    def parks(self):
        print(f"{self.name} is the pearl of Africa.")
country1 = Country('Uganda','Kamapla','5.98 million people')
country1.parks()
class Continent:
    def __init__(continent,A,B,C):
        continent.name = A
        continent.lakes = B
        continent.rivers = C  
    def nice(self):
        print(f"{self.name} is  beautiful.")
continent1 = Continent('Africa','Victoria','Nile')
continent1.nice() 