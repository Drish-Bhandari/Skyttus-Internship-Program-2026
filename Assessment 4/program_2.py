# Python Conditional Statements	

# # 1.Check if a person is eligible to vote (age ≥ 18).
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# # 2.Grade calculator based on marks: 90+ = A, 80+ = B, else C.
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     grade = 'A'
# elif marks >= 80:
#     grade = 'B'
# else:
#     grade = 'C'
# print(f"Your grade is: {grade}")

# # 3.Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
# while  True:
#     light_color = input("Enter the traffic light color (Red, Yellow, Green): ").lower()
#     if light_color == "red":
#         print("Stop")
#     elif light_color == "yellow":
#         print("Wait")
#     elif light_color == "green":
#         print("Go")
#     else:
#         print("Invalid traffic light color.")
#     ans = input("Do you want to continue? (yes/no): ").lower()
#     if ans == 'yes':
#         continue
#     else:
#         break  


# # 4.ATM withdrawal check: sufficient balance or not.
# balance = 2000.0
# amount = float(input("Enter the amount to check: "))
# if amount <= balance:
#     print("Sufficient balance")
# else:
#     print("Insufficient balance.")

# # 5.Check if a number is positive, negative, or zero.
# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# # 6.Check if a number lies within a given range.
# num = int(input("Enter a number: "))
# lower_bound = int(input("Enter the lower bound of the range: "))
# upper_bound = int(input("Enter the upper bound of the range: "))
# if lower_bound <= num <= upper_bound:
#     print("The number lies within the given range.")
# else:
#     print("The number does not lie within the given range.")

# # 7.Username & password verification.
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "12345":
#     print("Login successful.")
# else:
#     print("Invalid username or password.")

# # 8.Electricity bill calculator based on units consumed.
# units = int(input("Enter the number of units consumed: "))
# if units <= 100:
#     bill = units * 7.5
# elif units <= 200:
#     bill = 100 * 5 + (units - 100) * 9.5
# else:
#     bill = 100 * 7.5 + 100 * 9.5 + (units - 200) * 11.5
# print(f"Your electricity bill is: {bill}")

# # 9.Simple calculator (add, subtract, multiply, divide).
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     result = "Invalid operation"
# print(f"Result: {result}")

# # 10.Check type of triangle (equilateral, isosceles, scalene).
# side1 = float(input("Enter the first side of the triangle: "))
# side2 = float(input("Enter the second side of the triangle: "))
# side3 = float(input("Enter the third side of the triangle: "))
# if side1 == side2 == side3:
#     print("The triangle is equilateral.")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")
