# Error Handling

# # 1.Write a program to handle division by zero error.
# num1 = 10
# num2 = 0
# try:
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# # 2,Write a program to handle invalid integer input.
# input = input("Enter an integer: ")
# try:
#     value = int(input)
#     print("You entered:", value)
# except ValueError:
#     print("Error: Invalid integer input.")

# # 3.Write a program to open a file and handle the “file not found” error.
# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("Error: File not found.")

# # 4.Write a program to demonstrate multiple exception blocks.
# try:
#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid integer input.")

# 5.Write a program to use finally for resource cleanup.
# try:
#     file = open("sample.txt", "r")
#     content = file.read()
#     print(content)

# except FileNotFoundError:
#     print("File not found.")

# finally:
#     file.close()
#     print("File closed successfully.")


# # 6.Write a program to create a custom exception for invalid age (<18).
# age = int(input("Enter your age: "))

# try:
#     if age < 18:
#         raise Exception("Age must be 18 or above.")
#     print("Age is valid.")
# except Exception as e:
#     print("Error:", e)

# # 7.Write a program to handle IndexError when accessing a list.
# list = [1, 2, 3, 4, 5]
# index = int(input("Enter an index: "))
# try:
#     print(f"Element at index {index} is: {list[index]}")
# except IndexError:
#     print("Error: Index out of bounds.")

# # 8.Write a program that takes two numbers and handles all possible errors.
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter valid numbers.")

# # 9.Write a program to log errors to a file instead of printing them.
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("Result:", result)

# except Exception as e:
#     file = open("error.txt", "a")
#     file.write(str(e) + "\n")
#     file.close()

# 10.Write a program that validates an email format and raises an exception for invalid ones.
import re
email = input("Enter your email: ")
try:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise Exception("Invalid email format.")
    print("Email is valid.")
except Exception as e:
    print("Error:", e)
 