# Python loops

# # 1.Print numbers from 1 to 10.
# print("Number from 1 to 10 :")
# for i in range(1,11):
#     print(i)

# # 2.Display multiplication table for a given number.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#   print(f"{number} x {i} = {number * i}")

# # 3.Find factorial of a number.
# num = int(input("Enter a number to find factorial: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"The factorial of {num} is {factorial}") 

# # 4.Generate the first N Fibonacci numbers.
# num = int(input("Enter the number to generate Fibonacci series: "))
# fib_sequence = [0, 1]
# for i in range(2, num):
#     next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
#     fib_sequence.append(next_fib)
# print(f"The first {num} Fibonacci numbers are: {fib_sequence}")

# # 5.Check if a number is prime.
# number = int(input("Enter a number to check if it is prime: "))
# for i in range(2, int(number**0.5) + 1):
#     if number % i == 0:
#         print(f"{number} is not a prime number.")
#         break
# else:
#     print(f"{number} is a prime number.")

# # 6.Reverse a number (e.g., 123 → 321).
# num = int(input("Enter a number to reverse: "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(f"The reversed number is: {reversed_num}")

# # 7.Count digits in a number.
# number = int(input("Enter a number to count its digits: "))
# count = 0
# while number > 0:
#     number //= 10
#     count += 1    
# print(f"The number of digits is: {count}")

# # 8.Find sum of even numbers between 1–100.
# sum = 0
# for i in range(2, 101, 2):
#     sum += i
# print(f"The sum of even numbers between 1 and 100 is: {sum}")

# # 9.Print a pyramid pattern.
# rows = int(input("Enter the number of rows for the pyramid pattern: "))
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))

# 10.Find all divisors of a number.
number = int(input("Enter a number to find all divisors: "))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print(f"The divisors of {number} are: {divisors}")
