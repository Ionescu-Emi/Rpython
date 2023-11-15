import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
'''
c=Circle(1)
print("Circle area:",c.area())
print("Circle perimeter:",c.area())
r=Rectangle(5,10)
print("Rectangle area:",r.area())
print("Rectangle perimeter:",r.area())
t=Triangle(1,1,1)
print("Rectangle area:",t.area())
print("Rectangle perimeter:",t.area())
'''

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")




class SavingsAccount(Account):
    def add_nmonths_interest(self,n):
        for i in range(n):
            self.balance=self.balance* 0.05+self.balance
'''
acsav=SavingsAccount(1,0)
acsav.deposit(100)
print("Account balance:",acsav.balance)
acsav.withdrawal(50)
print("Account balance:",acsav.balance)
acsav.add_nmonths_interest(5)
print("Account balance:",acsav.balance)
'''
class CheckingAccount(Account):
    pass
'''
acchck=CheckingAccount(1,0)
acchck.deposit(100)
print("Account balance:",acchck.balance)
acchck.withdrawal(50)
print("Account balance:",acchck.balance)
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self):
        pass


class Car(Vehicle):
    def mileage(self):
        return 30  # Assuming 30 miles per gallon
    def towing_capacity(self):
        return 10


class Motorcycle(Vehicle):
    def mileage(self):
        return 50  # Assuming 50 miles per gallon
    def towing_capacity(self):
        return 10


class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def towing_capacity(self):
        return 1000
    def mileage(self):
        return 10  # Assuming 30 miles per gallon
'''
tr=Truck("Truck1","Model1",2007)
print("Truck towing cap",tr.towing_capacity())
print("Truck mileage",tr.mileage())
mc=Motorcycle("Motorcycle1","Model1",2008)
print("Motorcycle towing cap",mc.towing_capacity())
print("Motorcycle mileage",mc.mileage())
car=Car("Toyota","Model1",2006)
print("Car towing capacity",car.towing_capacity())
print("Motorcycle mileage",car.mileage())
'''

class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.has_book = True

    def check_out(self):
        if self.has_book:
            self.has_book = False
            print(f"{self.title} is checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if not self.has_book:
            self.has_book = True
            print(f"{self.title} is returned.")
        else:
            print(f"{self.title} is already returned.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")


class Book(LibraryItem):
    def __init__(self, title, author, publication_year, numpages):
        super().__init__(title, author, publication_year)
        self.num_pages = numpages
    def display_info(self):
        super().display_info()
        print(f"Number of pages", {self.num_pages})



class DVD(LibraryItem):
    def __init__(self, title, director, release_year, duration):
        super().__init__(title, director, release_year)
        self.duration = duration
    def display_info(self):
        super().display_info()
        print(f"Duration ", {self.duration})


class Magazine(LibraryItem):
    def __init__(self, title, publisher, publication_year, issue_number):
        super().__init__(title, publisher, publication_year)
        self.issue_number = issue_number
    def display_info(self):
        super().display_info()
        print(f"Issue_number", {self.issue_number})
'''
mag1=Magazine("Title","Publisher",2006,"ISBN1245")
mag1.display_info()
dvd1=DVD("Title","Director",2005,90)
dvd1.display_info()
book1=Book("Title","Author",2007,300)
book1.display_info()
book1.check_out()
book1.return_item()
book1.return_item()
book1.check_out()
book1.check_out()
'''