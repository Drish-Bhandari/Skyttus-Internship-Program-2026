# Python: Functions	

# # 1.Function to check if a number is prime.
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# number = int(input("Enter a number to check if it's prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# # 2.Function to reverse a string.
# def reverse_string(s):
#     return s[::-1]
# input_string = input("Enter a string to reverse: ")
# reversed_string = reverse_string(input_string)
# print("Reversed string:", reversed_string)


# # 3.Function to find factorial.
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(2, n + 1):
#             fact *= i
#         return fact
# num = int(input("Enter a number to find its factorial: "))
# fact1 = factorial(num)
# print(f"Factorial of {num} is: {fact1}")


# # 4.Function to calculate simple interest.
# def simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time period in years: "))
# interest = simple_interest(principal, rate, time)
# print(f"Simple interest is: {interest}")


# # 5.Function to check if a word is palindrome.
# def is_palindrome(word):
#     return word == word[::-1]
# word = input("Enter a word to check if it's a palindrome: ")
# if is_palindrome(word):
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")


# # 6.Function to count vowels in a string.
# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for x in string:
#         if x in vowels:
#             count += 1
#     return count
# input_string = input("Enter a string to count vowels: ")
# vowel_count = count_vowels(input_string)    
# print(f"Number of vowels in the string: {vowel_count}")


# # 7.Function to merge two lists.
# def merge_lists(list1, list2):
#     return list1 + list2
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged_list = merge_lists(list1, list2)
# print("Merged list:", merged_list)


# # 8.Function to find GCD of two numbers.
# def find_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("GCD is:", find_gcd(num1, num2))


# # 9.Function to find area of rectangle.
# def area_of_rectangle(length, width):
#     return length * width
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = area_of_rectangle(length, width)
# print(f"The area of the rectangle is: {area}")  

# 10.Function to check Armstrong number.
def is_armstrong(number):
    # Calculate the number of digits
    num_of_digits = len(str(number))
    sum_of_powers = 0

    temp_num = number
    while temp_num > 0:
        digit = temp_num % 10  # Extract the last digit
        sum_of_powers += digit ** num_of_digits # Raise to power of n and add
        temp_num //= 10 # Remove the last digit

    # Compare the final sum with the original number
    return sum_of_powers == number

num_to_check = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num_to_check):
    print(f"{num_to_check} is an Armstrong number.")
else:
    print(f"{num_to_check} is not an Armstrong number.")
