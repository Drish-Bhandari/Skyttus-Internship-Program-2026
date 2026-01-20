score = 0

print("Welcome to the Quiz Game!\n")

# Question 1
print("1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Chennai")
print("d) Kolkata")
ans = input("Enter your answer: ")

if ans.lower() == "b":
    score += 1

# Question 2
print("\n2. Which language is used for web development?")
print("a) Python")
print("b) Java")
print("c) HTML")
print("d) C")
ans = input("Enter your answer: ")

if ans.lower() == "c":
    score += 1

# Question 3
print("\n3. What is 5 + 3?")
print("a) 5")
print("b) 8")
print("c) 10")
print("d) 15")
ans = input("Enter your answer: ")

if ans.lower() == "b":
    score += 1

# Final Result
print("\nQuiz Finished!")
print("Your Score:", score, "/ 3")
