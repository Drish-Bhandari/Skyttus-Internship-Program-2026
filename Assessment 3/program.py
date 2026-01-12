# String fuctions
# 1.take a string and print its length
# x = input("Enter string to count length : ")
# print("Length:",len(x))

# 2.Convert a sentence to lowercase
# text = input("Enter a sentence:")
# print("To lowercase : ", text.lower())

# 3.Replace space with underscore in string
# text = "I am learning Python"
# string = text.replace(" ","_")
# print(string)

# 4.Extract the first and last character of string
# text = "Drish"
# print("First character: ",text[0])
# print("last character: ",text[-1])

# 5.Reverse a string using slicing
# text = "Python"
# print("Reversed String:",text[::-1])

# 6.count how many times a letter appear in string
# text = "Drish Bhandari"
# print("Count:", text.count("i"))

# 7.Check if a word present is a sentence
# text = "I am learning Python"
# word_to_find = "Python"
# words = text.split()
# if word_to_find in words:
#     print("present")
# else:
#     print("not present")

# 8.Take name & age and print using f-string formatting.
# name= input("Enter name:")
# age = int(input("Enter age:"))
# print(f"Your name {name} and your age {age}")

# 9.Remove extra spaces from the start and end of a string.
# text = "   I am learning Python   "
# print("string:",text.strip())

# 10.Join a list of words into a single string with - between them.
# text = ("I","am","learning","python")
# x = "-".join(text)
# print(x)


# list functions

# 1.Create a list of your 5 favorite movies.
# favorite_movies = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]

# 2.Add a new movie to the list.
# favorite_movies.append("Movie6")
# print(favorite_movies)

# 3.Remove the first movie from the list.
# favorite_movies.remove("Movie1")
# print(favorite_movies)

# 4.Sort a list of numbers in ascending order.
# list1 = [9,8,7,6,5,4,3,2,1]
# list1.sort()
# print(list1)

# 5.Reverse a list.
# list1 = [9,8,7,6,5,4,3,2,1]
# list1.reverse()
# print(list1)

# 6.Find the largest number in a list.
# list1 = [9,8,7,6,5,4,3,2,1]
# largest = max(list1)
# print(largest)

# 7.Merge two lists into one.
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list3 = list1 + list2
# print("merged list: ",list3)

# 8.Access the last element of a list without using index number.
# list1 = [9,8,7,6,5,4,3,2,1]
# last_element = list1[-1]
# print(last_element)

# 9.Create a nested list and access a specific inner element.
# list1 = [1,2,3,[4,5,6]]
# # assessing element "4"
# element = list1[3][0]
# print(element)

# 10.Count how many times an element appears in a list.
# list1 = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# x = list1.count(9)
# print("Count:",x)


# tuple and set

# 1.Create a tuple with 5 numbers.
# my_tuple = (1,2,3,4,5)

# 2.Access the third element in a tuple.
# print("Third element:",my_tuple[2])

# 3.Unpack a tuple into separate variables.
# a,b,c,d,e = my_tuple
# print(a)
# print(b)

# 4.Create a set of 5 fruits.
#fruits = {"apple", "banana", "cherry","mango","orange"}

# 5.Add a new fruit to the set.
# fruits.add("pineapple")
# print("Added element:",fruits)

# 6.Remove an element from a set.
# fruits.remove("pineapple")
# print("Removed element",fruits)

# 7.Find union of two sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.union(set2)
# print(set3)

# 8. Find intersection of two sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

# 9.Check if one set is subset of another.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.issubset(set2)
# print(set3)

# 10.Convert a list with duplicate values into a set to remove duplicates.
# list1 = [1,2,3,4,5,6,7,8,9,1,2,4,5,3,6]
# set1 = set(list)
# print(set)


# Dictionary functios

# 1.Create a dictionary storing student names and marks.
#dist = {"student1": 80,"student2":90,"student3":75}

# 2.Add a new key-value pair to an existing dictionary.
# dist["student4"] = 85
# print(dist)

# 3.Delete a key-value pair from a dictionary.
# del dist["student4"]
# print(dist)

# 4.Merge two dictionaries into one.
# dist1 = {"student1": 80,"student2":90,"student3":75}
# dist2 = {"student4": 65,"student5":87,"student6":77}
# dist3 = dist1 | dist2
# print("Merged dist: ",dist3)

# 5.Check if a key exists in a dictionary.
# dist1 = {"student1": 80,"student2":90,"student3":75}
# key = "student2"
# if key in dist1 :
#     print(f"{key} exists in dictonary")
# else:
#     print("not exists")

# 6.Count word frequency in a given string using a dictionary.
# text = "hello world hello python world"
# words = text.split()
# word_counts = {}

# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
# print(word_counts)

# 7.Find the key with the maximum value in a dictionary.
# dict = {"student1": 80,"student2":90,"student3":75}
# max_key = max(dict,key=dict.get)

# print(f"The key with the maximum value is: {max_key}")

# 8.Reverse keys and values in a dictionary.
# dict = {"student1": 80,"student2":90,"student3":75}
# reversed_dict = {}
# for key, value in dict.items():
#     reversed_dict[value] = key

# print(reversed_dict)


# 9.Update the value for a specific key.
# dict1 = {"student1": 80,"student2":90,"student3":75}
# dict1["student1"] = 85
# print(dict1)

# 10.Convert a list of tuples into a dictionary.
# list1 = [("student1",80),("student2",90),("student3",75)]
# dict1 ={}
# for key, value in list1:
#     dict1[key] = value
# print(dict1)