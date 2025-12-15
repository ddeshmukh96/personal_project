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

book1.book_details()