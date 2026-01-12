# tuple and set

# 1.Create a tuple with 5 numbers.
# my_tuple = (1,2,3,4,5)

# 2.Access the third element in a tuple.
# print("Third element:",my_tuple[2])

# 3.Unpack a tuple into separate variables.
# a,b,c,d,e = my_tuple
# print(a)
# print(b)

# # 4.Create a set of 5 fruits.
# fruits = {"apple", "banana", "cherry","mango","orange"}

# # 5.Add a new fruit to the set.
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

# OR
# dict1 = dict(list1)
# print(dict1)