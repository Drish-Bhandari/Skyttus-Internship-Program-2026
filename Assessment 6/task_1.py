# # 1.Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.speed = 0 

#     def accelerate(self):
#         self.speed += 10
#         print("Speed increased to:", self.speed)

#     def brake(self):
#         if self.speed >= 10:
#             self.speed -= 10
#         else:
#             self.speed = 0
#         print("Speed decreased to:", self.speed)

# car1 = Car("Toyota", "Innova")

# car1.accelerate()
# car1.accelerate()
# car1.brake()

# # 2.Create a BankAccount class with deposit and withdraw methods.
# class BankAccount:
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("Current Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Current Balance:", self.balance)
#         else:
#             print("Insufficient balance")

# account = BankAccount("Rahul", 1000)

# account.deposit(500)
# account.withdraw(300)
# account.withdraw(2000)


# # 3.Create a Student class with a method to calculate average marks.
# class student:
#     def __init__(self, maths, english, science):
#         self.maths = maths
#         self.english = english
#         self.science = science
    
#     def average_marks(self):
#         average = (self.maths + self.english + self.science)/3
#         print("Average marks :", average)
        
# student1 = student(90,85,75)

# student1.average_marks()


# # 4. Create a Rectangle class with methods to find area and perimeter.
# class rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.heigth = height
    
#     def area(self):
#         return self.heigth * self.width
    
#     def perimeter(self):
#         return 2 * (self.heigth + self.width)
    
# rect = rectangle(10,5)

# print("Area of Rectangle: ",rect.area())
# print("Perimeter of Rectangle: ", rect.perimeter())


# # 5.Create an Employee class that displays salary details. 
# class employee:
#     def __init__(self, employee_id ,emplyoee_name, salary):
#         self.employee_id = employee_id
#         self.employee_name = emplyoee_name
#         self.salary = salary

#     def salary_details(self):
#         print("Employee ID:", self.employee_id)
#         print("Employee Name:", self.employee_name)
#         print("Salary:", self.salary)

# emp = employee(101, "Jay", 35000)

# emp.salary_details()       

# # 6.Create a Book class to store title, author, and price, and display details.
# class book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
    
#     def book_details(self):
#         print("Book Title:",self.title)
#         print("Author: ", self.author)
#         print("Price: ", self.price)
    
# book1 = book("Dune", "Frank Herbert", 1000)

# book1.book_details()

# # 7.Create a Circle class to find area and circumference. 
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         area1 = 3.14 * (self.radius ** 2)
#         print("Area of Circle: ",area1)
    
#     def circumference(self):
#         circum = 2 * 3.14 * self.radius
#         print("circumference of circle: ",circum)

# crc = circle(5)

# crc.area()
# crc.circumference()


# # 8.Create a Laptop class with a method to apply discounts on price. 
# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def discount(self, discount_percent):
#         discount_amount = (discount_percent / 100) * self.price
#         self.price -= discount_amount
#         print("Brand:", self.brand)
#         print("Price after discount:", self.price)

# laptop1 = Laptop("HP", 60000)

# laptop1.discount(10)


# # 9.Create a Flight class with seat booking functionality.
# class Flight:
#     def __init__(self, flight_no, total_seats):
#         self.flight_no = flight_no
#         self.total_seats = total_seats
#         self.booked_seats = 0

#     def book_seat(self, seats):
#         if self.booked_seats + seats <= self.total_seats:
#             self.booked_seats += seats
#             print(seats, "seat(s) booked successfully.")
#         else:
#             print("Not enough seats available.")

#     def available_seats(self):
#         return self.total_seats - self.booked_seats

# flight = Flight("AI-202", 100)

# flight.book_seat(5)
# flight.book_seat(98)

# print("Available seats:", flight.available_seats())


# # 10. Create a Shop class with a method to add and list products.
# class shop:
#     def __init__(self, shop_name):
#         self.shop_name = shop_name
#         self.products = []
    
#     def add_products(self, product_name):
#         self.products.append(product_name)
#         print(product_name," added to cart")
    
#     def list_products(self):
#         print(f"Products available in {self.shop_name }:")
#         for product in self.products:
#             print("-", product)

# my_shop = shop("City Mobile")

# my_shop.add_products("Keyboard")
# my_shop.add_products("mouse")
# my_shop.add_products("Pendrive")

# my_shop.list_products()
        