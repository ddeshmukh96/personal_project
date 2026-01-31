"""
Car
Engine Capacity INT
No. of seats INT
Number Plate STRING
Chassis No. STRING
Color STRING

Animal
no. of legs INT
type of diet BOOLEAN
Species type STRING
gender STRING/BOOLEAN

Chair
no. of legs INT
color STRING
size  TUPLE OF INT,INT,INT
volume  INT
pack_size  PAIR OF INT,STRING
type  STRING

"""

class Chair:
    def __init__(self, legs, color, size, volume, pack_size, chair_type):
        self.legs=legs
        self.color=color
        self.size=size
        self.volume=volume
        self.pack_size=pack_size
        self.chair_type=chair_type

    def show_details(self):
        print("Type:", self.chair_type)
        print("Color:", self.color)
        print("Legs:", self.legs)
        print("Size:", self.size)
        print("Volume:", self.volume)
        print("Pack_size:", self.pack_size)

chair1=Chair(
    4,
    "Cremson Blue",
    (40,30,90),
    108000,
    (1,"Box"),
    "Office Chair"
)

# chair1.show_details()

class Book:
    def __init__(self, book_type, book_purpose, writer_name, cost):
        self.book_type=book_type
        self.book_purpose=book_purpose
        self.writer_name=writer_name
        self.cost=cost
    
    def book_details(self):
        print("Purpose_of_book:", self.book_purpose)
        print("Type_of_book:", self.book_type)
        print("Writer_of_book:", self.writer_name)
        print("Book_cost:", self.cost)

book1=Book(
    book_type="Educational",
    book_purpose="To learn Mathematics in simpler way",
    writer_name="HC Verma",
    cost=550
)

# book1.book_details()

# Learning Contructor types
class Student:

    # prameterized constructors
    def __init__(self,name,roll_no,marks):
        self.name_of_student=name
        self.roll_no_of_student=roll_no
        self.marks_scored=marks

s1=Student(
    name="Dhananjay",
    roll_no=9,
    marks=93.6
)

s2=Student(
    name="Pawan",
    roll_no=11,
    marks=96
)

s3=Student("Sarvesh",29,90)

# print(s1.marks_scored,s1.name_of_student)
# print(s2.name_of_student)
# print(s3.roll_no_of_student)

# Remember that the objects call's variables referencing 2nd function
# hence gets executed and no reference vai objects for 1 st function
#  so the 1st function is not executed

class Democlass:
    # Default constructor
    def __init__(self):
        print("Cholas were undefeated")

# object1=Democlass()

# Learning Class Attribute and Object Attribute
class Students:

    # Class Attribute
    college_name="PCCOE Pune"
    name="Anonyomus"

    def __init__(self,name,roll_no,marks):
        # obj attribute
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

# s1=Students("Karan",12,92)
# print(s1.name)
# print(Students.college_name)  # calling via Class name
# print(s1.college_name)        # Calling via Obj

# output : Karan (if class attribute and object attribute has
#                 same variable name remember Objects attribute's
#                 precedence is always higher than the Class attribute)

# Understanding Constructors and Methods
# Methods are functions that belongs to class
class C_student:

    # constructor
    def __init__(self,name,city):
        self.name=name
        self.city=city
    
    # Methods
    def welcome(self):
        print("Hello",self.name)

    def get_city(self):
        return self.city

c_s1=C_student("Atharva","Pune")

# print(c_s1.name)
# # calling via method name
# c_s1.welcome()           
# print(c_s1.get_city())

"""
Create student class that takes name and marks
of 3 subjects as arguments in constructor.Then
create a method to print the average

"""

""" Method 1 -  provide marks separately """

class School_student1:

    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def sub_average(self):
        avg=(self.m1+self.m2+self.m3)/3
        return avg

s1_s1=School_student1("Vikrant",89,85,92)
s1_s2=School_student1("Sakshi",93,87,96)
s1_s3=School_student1("Shivani",85,94,98)

# print(round(s1_s1.sub_average(),2),round(s1_s2.sub_average(),2),round(s1_s3.sub_average(),2))

"""" Method 2 - assuming marks as a list """

class School_student2:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    # Static Method : when we don't want any reltn with the instance attr
    @staticmethod  # this is called decorator and works at Class Level
    def warm_msg():
        print("Hey your avg is:")

    def get_avg(self):
        initial_sum=0
        for i in self.marks:
            initial_sum=i+initial_sum
        avg=initial_sum/len(self.marks)
        return round(avg,2)

s2_s1=School_student2("Vikrant",[89,85,92])
s2_s2=School_student2("Sakshi",[93,87,96])
s2_s3=School_student2("Shivani",[85,94,98])

# School_student2.warm_msg()
# print(s2_s1.get_avg(),s2_s2.get_avg(),s2_s3.get_avg())

# Just additional practice
class School_student3:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    # Static Method
    @staticmethod
    def warm_msg():
        print("Hey your avg score is:")

    def get_avg(self):
        School_student3.warm_msg()
        initial_sum=0
        for i in self.marks:
            initial_sum=i+initial_sum
        avg=initial_sum/len(self.marks)
        print(round(avg,2))

s3_s1=School_student3("Vikrant",[89,85,92])
s3_s2=School_student3("Sakshi",[93,87,96])
s3_s3=School_student3("Shivani",[85,94,98])

# s3_s1.get_avg()
# s3_s2.get_avg()
# s3_s3.get_avg()


# If I want to update / change name of Vikrant to "Shubham"

s2_s1.name="Shubham"

# print(s2_s1.name)

# calling functions by Static method 

# s2_s1.warm_msg()
# School_student2.warm_msg()


# Learning Abstraction (not real example)

"""
Hiding implemention details of a class and showing the essential features
of class to an user
"""
class MyCar:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

# c1=MyCar()
# c1.start()  
""" at this line we get the "car started" so understand this as
    user never came across the implemention i.e. statement/code
    one has written so only the output has been seen by user
            """

""" 
Practice Problem
Create account class with 2 attributes: balance and account no.
    Create methods for debit, credit and printing balance """

class Account:

    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    # debit function
    def debit(self,d_amount):
        self.balance=self.balance-d_amount
        print("Rs.",d_amount,"was debited from your account")
        print("Total Balance = ",self.get_balance())

    def credit(self,c_amount):
        self.balance+=c_amount
        print("Rs.",c_amount,"is credited in your account")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

# acc1=Account(10000,5308759156)
# acc1.debit(1250)
# acc1.credit(450)
# acc1.credit(55000)
# acc1.debit(7500)

""" del keyword  """

class Don:

    def __init__(self,name):
        self.name = name

d1=Don("Chetan")
# print(d1.name)
del d1.name
# print(d1.name)

""" # Learning Public and Private through oops"""

""" Note: Variables/Attributes and Methods can be made private by "__" """

class Student_account:

    def __init__(self,name,acc_pass):
        self.name=name               # Public : Accessible outside class
        self.__acc_pass=acc_pass     # Private : Not acc. outside class
                                     #           but can be accesed by the
                                     #           internal functions
    def reset_pass(self):
        print(self.__acc_pass)

# s_acc1=Student_account("Sharvari","S#96KSD")
# print(s_acc1.name)
# s_acc1.reset_pass()

class Person:
    __name="anonymus"

    def __hello(self):
        print("Hello World")
    
    def get_hello(self):
        self.__hello()

# p1=Person()
# p1.get_hello()

""" Learning Inheritance  """

""" Single Level Inheritance     """
class Car:

    color="Black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota_car(Car):

    def __init__(self,name):
        self.name=name

car1=Toyota_car("Fortuner")
car2=Toyota_car("Hyryder")

# print(car1.name)
# print(car1.color)

""""  Multi-Level Inheritance   """

class Car1:

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota_Car1(Car1):
    def __init__(self,model_name):
        self.model_name=model_name

class Fortuner_car1(Toyota_Car1):
    def __init__(self,engine_type):
        self.engine_type=engine_type

c1=Fortuner_car1("Diesel Engine")
c2=Toyota_Car1("Fortuner")
# c1.start()
# print(c1.engine_type)
# print(c2.model_name)
# c2.stop()

""""  Multiple Inheritance   """

class A:
    def displayA(self):
        print("Sleep is very essential")

class B:
    def displayB(self):
        print("This boosts Immune system")

class C(A,B):
    def displayC(self):
        print("Hope you will do this")

p_1=C()
# p_1.displayC()
# p_1.displayB()
# p_1.displayA()

""" Super method

super() method is used access the methods of parent class

Example through single heritance

"""

class N_car:

    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped")

class Car_Model(N_car):
    def __init__(self,name,type):
        super().start()
        self.name=name
        super().__init__(type)

# car_1=Car_Model("Hyryder","Mild Electric")

# print(car_1.name,car_1.type)


"""  Learnign Class Method   """

class N_person:
    name="anonymus"

    # def changename(self,name):
    #     self.__class__.name=name
    #     # N_person.name=name or self.__class__.name=name

    @classmethod
    def changename(cls,name):
        cls.name=name

person1=N_person()
person1.changename("Kushal")
# print(person1.name)
# print(N_person.name)

""" 
class N_person:
    name="anonymus"

    def changename(self,name):
        self.name=name

person1=N_person()
person1.changename("Kushal")
print(person1.name)       O/P : Kushal
print(N_person.name)      o/p : anonymus


from above eg. we can clearly see that as constructor is not used 
the obj/instance can't be accessed through Class since it takes 0
positional argument

As a result we have to first make an obj then use that obj to call method
name and provide the positional argument and then print whatever
output we want

If same thing called by class name we get different output since for the
object we created a new variable called self.name hence no relation
between it and the anonymus

But if someone wants to change name="anonymus" through the obj i.e.
person1 here then we use class methods

In-short we want to change the Class attribute values

Way 1 : Instead of writing self.name we write N_person.name

Code:
class N_person:
    name="anonymus"

    def changename(self,name):
        N_person.name=name

person1=N_person()
person1.changename("Kushal")
print(person1.name)             o/p : Kushal
print(N_person.name)            o/p : Kushal

Way 2 : Showing N_person.name as self.__class__.attribute

class N_person:
    name="anonymus"

    def changename(self,name):
        self.__class__.name=name

person1=N_person()
person1.changename("Kushal")
print(person1.name)
print(N_person.name)

Note: If we assigned a name at  self.__class__.name = "Rahul", all things
      gets overide and we get output as Rahul for oth print 
"""

"""  Learning @Property Decorator"""

class Science:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

    # # way1 for getting updated percentage (general approach)
    # def cal_percentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

    @property  # to inherit all variables from one fnctn to this functn
    def percentage(self):
        return (str((self.phy+self.chem+self.math)/3) + "%")


# stu1=Science(98,97,95)
# print(stu1.percentage)
# stu1.phy=86
# # stu1.cal_percentage()
# print(stu1.percentage)

"""
Imagine a scenario where tye teacher remind that phy marks should be
86 instead of 98 then I would update the phy marks for stu1

So I write code as :
class Science:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

stu1=Science(98,97,95)
print(stu1.percentage)
stu1.phy=86                o/p: 96.67%
print(stu1.phy)            o/p: 86
print(stu1.percentage)     o/p: 96.67

but when I updated % for phy it should have given me the outout as 92.67%
since it is using the attributes from line 551 not the updated % for phy

For getting this to becorrect we use the property decorator
"""

"""   Learning Polymorphism     """

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        # print(self.real,"i +",self.img,"j")
        sign = "+" if self.img >= 0 else "-"
        print(f"{self.real}i {sign} {abs(self.img)}j")
    
    def __add__(self,com2):
        new_real=self.real+com2.real
        new_img=self.img+com2.img
        return Complex(new_real,new_img)
    
    def __sub__(self,com2):
        new_real=self.real-com2.real
        new_img=self.img-com2.img
        return Complex(new_real,new_img)

com1=Complex(2,5)
# com1.showNumber()

com2=Complex(7,9)
# com2.showNumber()

com3=com1+com2
# com3.showNumber()

com4=com1-com2
# com4.showNumber()

""" 
To create complex number

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

com1=Complex(2,5)
com1.showNumber()    o/p: 2i + 5j

com2=Complex(7,3)
com2.showNumber()    o/p: 7i + 3j

@ Now if someone wants to add com1 & com2

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,com2):
        new_real=self.real+com2.real
        new_img=self.img+com2.img
        return Complex(new_real,new_img)

com1=Complex(2,5)
com1.showNumber()    o/p: 2i + 5j

com2=Complex(7,3)
com2.showNumber()    o/p: 7i + 3j

com3=com1.addNum(com2)
com3.showNumber()    o/p: 9i + 8j

@ But someone who don't want to create com3 by calling the addNum functn
so now we use " Dunder functions " or basically Polymorphism comes here

Code:

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,com2):
        new_real=self.real+com2.real
        new_img=self.img+com2.img
        return Complex(new_real,new_img)


com1=Complex(2,5)
com1.showNumber()    o/p: 2i + 5j

com2=Complex(7,3)
com2.showNumber()    o/p: 7i + 3j

com3=com1 + com2
com3.showNumber()    o/p: 9i + 8j

"""


""" 
Practice Questions

Define a Circle Class to create a circle with radius using the constructor
Define a Area() method of the class which which calculates area of circle
Define a Perimeter() method of the class which allows to calculate
perimeter of circle

"""

class Circle:

    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return (22/7)*(self.radius**2)
    
    def Perimeter(self):
        return 2*(22/7)*self.radius


crl1=Circle(21)
# print(crl1.Area())
# print(crl1.Perimeter())

"""
Define a Employee class with attributes role, department and salary. This
class has showDetails() method
Create a Enineer class that inherits property from Employee and has
additional attributes : name & age

"""

class Employee:

    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print("Role = ",self.role)
        print("Department = ",self.dept)
        print("Salary = ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Senior PDE","Engineering Service", 750000)


engg1=Engineer("Sean", 27)

# engg1.showDetails()
# print(engg1.name)

""" 

Create a class called Order which stores items
and its cost
Use Dunder function __gt__() to convey that:
   order1 > order2 if price of order1 > price of order2

"""

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        