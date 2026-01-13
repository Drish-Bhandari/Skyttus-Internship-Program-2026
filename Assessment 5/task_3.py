# File Handling	

# # 1.Write a program to read a file and display its contents.
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print("File Contents:\n", content)
# except FileNotFoundError:
#     print("Error: File not found.")

# # 2.Write a program to count the number of lines in a file.
# try:
#     with open("sample.txt", "r") as file:
#         lines = file.readlines()
#         print(f"Number of lines in the file: {len(lines)}")
# except FileNotFoundError:
#     print("Error: File not found.")

# # 3.Write a program to count how many times each word appears in a file.
# try:
#     with open("sample.txt", "r") as file:
#         word_count = {}
#         for line in file:
#             words = line.split()
#             for word in words:
#                 word = word.lower().strip('.,!?;"()[]{}')  # Normalize the word
#                 if word in word_count:
#                     word_count[word] += 1
#                 else:
#                     word_count[word] = 1
#         print("Word Count:")
#         for word, count in word_count.items():
#             print(f"{word}: {count}")
# except FileNotFoundError:
#     print("Error: File not found.")

# # 4.Write a program to write 5 user-entered sentences to a file.
# sentences = []
# for i in range(5):
#     sentence = input(f"Enter sentence {i+1}: ")
#     sentences.append(sentence)

# with open("sample.txt", "a") as file:
#     for sentence in sentences:
#         file.write(sentence + "\n")

# print("Sentences written to sample.txt")

# # 5.Write a program to append a list of strings to an existing file.
# text = ["First string", "Second string", "Third string"]
# with open("sample.txt", "a") as file:
#     for s in text:
#         file.write(s + "\n")
# print("Strings appended to sample.txt")

# # 6.Write a program to read a file and print only lines containing a specific word.
# try:
#     with open("sample.txt", "r") as file:
#         word = input("Enter the word to search for: ")
#         for line in file:
#             if word in line:
#                 print(line)
# except FileNotFoundError:
#     print("Error: File not found.")

# # 7.Write a program to replace a specific word in a file and save changes.
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#     old_word = "file"
#     new_word = "txt file"
#     content = content.replace(old_word,new_word)

#     with open("sample.txt", "a") as file:
#         file.write(content)
# except FileNotFoundError:
#     print("Error: File not found.")

# # 8.Write a program to merge the contents of two text files into a third file.
# try:
#     with open("sample.txt", "r") as file:
#         content1 = file.read()
#     with open("sample2.txt", "r") as file:
#         content2 = file.read()
#     with open("merged_file.txt", "w") as file:
#         file.write(content1)
#         file.write(content2)
#     print("File merged successfully")
# except:
#     print("Error: File not found")

# # 9.Write a program to read a CSV file and display its content in a formatted way.
# import csv
# try:
#     with open("example.csv", "r") as file:
#         csv_reader = csv.reader(file)

#         for row in csv_reader:
#             print("\t".join(row))

# except FileNotFoundError:
#     print("Error: CSV file not found.")
   
# 10.Write a program to back up a file by copying its contents into another file.
try:
    with open("example.csv", "r") as file:
        content = file.read()
    with open("sample2.txt", "a") as file:
        file.write(content)
    print("File backed up successfully")
except FileNotFoundError:
    print("Error: CSV file not found.")