# # Modules & Libraries

# # 1.Create a custom math module and import it in another file.
# import mymaths

# print("Addition: ", mymaths.add(10,2))
# print("Subtraction: ", mymaths.subtract(10,2))
# print("Multiplicaton: ", mymaths.multiply(10,2))
# print("Division: ", mymaths.divide(10,2))


# 2.Create a module to perform string operations. 
# main.py

# import string

# text = input("Enter a string: ")

# print("Uppercase:", string.to_upper(text))
# print("Lowercase:", string.to_lower(text))
# print("Reversed:", string.reverse_string(text))
# print("Length:", string.string_length(text))


# # 3.Use random module to generate 5 random integers.
# import random

# for i in range(5):
#     print(random.randint(1, 100))


# # 4.Use datetime module to display current date and time. 
# import datetime

# current_datetime = datetime.datetime.now()

# print("Current Date and Time:", current_datetime)


# 5.Use math module to find factorial of a number.
# import math

# num = int(input("Enter a number: "))
# result = math.factorial(num)

# print("Factorial of", num, "is:", result)


# # 6.Create a package shapes with modules for circle and rectangle.
# from Shapes import circle, rectangle

# print("Circle Area:", circle.area(5))
# print("Circle Circumference:", circle.circumference(5))

# print("Rectangle Area:", rectangle.area(10, 4))
# print("Rectangle Perimeter:", rectangle.perimeter(10, 4))


# # 7.Import multiple functions from one module and use them.
# from mymaths import add, subtract, multiply

# print("Addition:", add(10, 5))
# print("Subtraction:", subtract(10, 5))
# print("Multiplication:", multiply(10, 5))


# # 8.Write a program to shuffle a list using random module.
# import random

# items = [1, 2, 3, 4, 5]

# random.shuffle(items)

# print("Shuffled list:", items)


# # 9.Write a program to calculate the difference between two dates.
# from datetime import date

# date1 = date(2026, 1, 1)
# date2 = date(2026, 1, 15)

# difference = date2 - date1

# print("Difference in days:", difference.days)


# # 10.Use os module to list files in a directory.
# import os

# path = "."

# files = os.listdir(path)

# print("Files in directory:")
# for file in files:
#     print(file)

 