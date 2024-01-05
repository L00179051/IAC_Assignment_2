'''
Python script for: Data Structures
Date: 13OCT2023
By: Shahanawaz Shaikh
'''

# Lists
list1 = [0, 1, 2, "Char0", "Char1", "CharLast"] # Unlike numerics, strings are to be specified in inverted colun
print(f"The length of the specified List is: ", len(list1))
print(f"Sliced elements from the list: ",list1[2:4:1])
print(f"Last character in the list: ",list1[-1])
# Lists - Concatenate
list2 = [3,4,5,"Char2","Char3"]
concatenatedList = list1 + list2
print(f"Concatenated list is: ",concatenatedList)
#lists - Nested
nestedList = [list1,list2]
print(f"Nested list is: ",nestedList)
print(list2[0])
list2[0] = 1
print(f"Editing the specific element in an array. After overwriting, the value is now: ", list2[0])
# Lists - CSV
csv1 = "Shahanawaz Shaikh,ATU,Letterkenny,2023"
print(f"Splitting values from a csv: ", csv1.split(","))

# Tuples
list3 = ["a","b"]   # Type - List
set1 = {"a","b"}    # Type - set
tuple1 = ("a","b")  # Type - tuple (immutable)
print(f"\n Type of list3: {type(list3)} \n Type of set1: {type(set1)} \n Type of tuple1: {type(tuple1)}")

# Methods
