# 1.Write a program to print your name, age and city in one line
name = "Drish"
age= 22
city = "Vapi"
print(f"Name:{name}  Age:{age}  City:{city}")

# 2.Take user input for two number and print their sum
a = int(input("Enter First Number:"))
b = int(input("Enter First Number:"))
add = a + b
print(f"{a} + {b} = {add}")

# 3.Write a program to convert temperature from celcius to fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")

# 4.Store your name in variable and print in upper case
name = "Drish"
print("Name :", name.upper())

# 5.Ask the user for their birth year and culculate there current age
birth_year = int(input("Enter birth year: "))
current_year = 2026
print("Current Age = ", current_year - birth_year)

# 6.Write a program to swap the value of two variable
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

# Swap the values
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

# 7.create a program to calculate the area of rectange from user input 
length = float(input("Enter the length of rectangle :"))
breath = float(input("Enter the length of rectangle :"))
area= length * breath 
print("Area of Rectangle = ", area)

# 8.Write a program to find number is positive or negative 
number = int(input("Enter number to check Positive or Negative :"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Number is 0")

# 9.Ask for two number and print their average
num1 = int(input("Enter 1st number to find average: "))
num2 = int(input("Enter 2nd number to find average: "))
avg = (num1 + num2) / 2
print("Average of two number is ",avg)
