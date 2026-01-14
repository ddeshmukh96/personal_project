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

class Student:
    # prameterizes constructors
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

class Democlass:
    # Default constructor
    def __init__(self):
        print("Cholas were undefeated")

# object1=Democlass()

class Students:
    college_name="PCCOE Pune"
    name="Anonyomus"

    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

s1=Students("Karan",12,92)
# print(s1.name)

# output : Karan (if class attribute and object attribute has
#                 same variable name remember Objects attribute's
#                 precedence is always higher than the Class attribute)

class C_student:

    def __init__(self,name,city):
        self.name=name
        self.city=city
    
    def welcome(self):
        print("Hello",self.name)

    def get_city(self):
        return self.city

c_s1=C_student("Atharva","Pune")

# print(c_s1.name)
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
    
    # Static Method
    @staticmethod  # this is called decorator
    def warm_msg():
        print("Hello World")

    def get_avg(self):
        initial_sum=0
        for i in self.marks:
            initial_sum=i+initial_sum
        avg=initial_sum/3
        return round(avg,2)

s2_s1=School_student2("Vikrant",[89,85,92])
s2_s2=School_student2("Sakshi",[93,87,96])
s2_s3=School_student2("Shivani",[85,94,98])

# print(s2_s1.get_avg(),s2_s2.get_avg(),s2_s3.get_avg())

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
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

# c1=Car()
# c1.start()  
""" at this line we get the "car started" so understand this as
    user never came across the implemention i.e. statement/code
    one has written so only the output has been seen by user
            """
# Create account class with 2 attributes: balance and account no.
# Create methods for debit, credit and printing balance

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

acc1=Account(10000,5308759156)
acc1.debit(1250)
acc1.credit(450)
acc1.credit(55000)
acc1.debit(7500)

