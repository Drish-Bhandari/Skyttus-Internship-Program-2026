# # Advanced OOPS

# # 1.Create a base class Animal and subclasses Dog and Cat.
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()


# # 2.Create a class hierarchy for Vehicle → Car → ElectricCar. 
# class vehicle:
#     def __init__(self, brand):
#         self.brand = brand
    
#     def show_brand(self):
#         print("Brand: ", self.brand)
    
# class car(vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def show_model(self):
#         print("Model: ",self.model)

# class electricCar(car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity
    
#     def show_battey(self):
#         print("Battery Capacity: ", self.battery_capacity)

# eCar = electricCar("Tesla", "Model 3", 75)

# eCar.show_brand()
# eCar.show_model()
# eCar.show_battey()


# # 3.Implement method overriding in a base and derived class. 
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# animal = Animal()
# dog = Dog()

# animal.sound()
# dog.sound()


# # 4.Demonstrate multiple inheritance with two parent classes.
# class Father:
#     def father_skill(self):
#         print("Father: Driving")

# class Mother:
#     def mother_skill(self):
#         print("Mother: Cooking")

# class Child(Father, Mother):
#     def child_skill(self):
#         print("Child: Playing")

# child = Child()

# child.father_skill()
# child.mother_skill()
# child.child_skill()


# # 5.Create a polymorphic function that works with different shapes.
# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5

# class Circle(Shape):
#     def area(self):
#         return 3.14 * 7 * 7

# # Polymorphic function
# def print_area(shape):
#     print("Area:", shape.area())

# rect = Rectangle()
# circle = Circle()

# print_area(rect)
# print_area(circle)


# # 6.Create a Bank system with SavingsAccount and CurrentAccount classes.
# class BankAccount:
#     def __init__(self, account_no, balance = 0):
#         self.account_no = account_no
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit: ", amount)
#         print("Balance: ", self.balance)
    
# class SavingAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdraw from Saving: ",amount)
#         else:
#             print("Insufficient Balance")
        
#         print("Balance: ",self.balance)

# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdraw from Saving: ",amount)
#         else:
#             print("Insufficient Balance")
        
#         print("Balance: ",self.balance)

# saving = SavingAccount(1234)
# current = CurrentAccount(5678)

# saving.deposit(2000)
# saving.withdraw(1000)

# current.deposit(3000)
# current.withdraw(2000)


# # 7. Create a class with private attributes and getter/setter methods
# class person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name
    
#     def set_name(self, name):
#         self.__name = name 


#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Invalid Age")
    
# p1 = person("Ram", 20)

# print("Name: ", p1.get_name())
# print("Age: ", p1.get_age())

# # modify age
# p1.set_age(25)
# print("Modified Age:", p1.get_age())


# # 8.Create a Teacher and Student class to show inheritance. 
# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

#     def display_teacher(self):
#         print("Teacher Name:", self.name)
#         print("Subject:", self.subject)


# class Student(Teacher):
#     def __init__(self, name, subject, roll_no):
#         super().__init__(name, subject)
#         self.roll_no = roll_no

#     def display_student(self):
#         print("Student Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Subject:", self.subject)


# student = Student("Ankit", "Maths", 23)

# student.display_student()


# # 9.Create a MusicPlayer class and subclass Spotify to override play method. 
# class MusicPlayer:
#     def play(self):
#         print("Playing music from Music Player")

# class Spotify(MusicPlayer):
#     def play(self):
#         print("Playing music from Spotify")

# player = MusicPlayer()
# Spotify_player = Spotify()

# player.play()
# Spotify_player.play()


# # 10.Demonstrate the use of super() in inheritance.
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)

# class Student(Person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

#     def show(self):
#         super().show()
#         print("Roll No:", self.roll_no)

# student = Student("Ankit", 101)

# student.show()
