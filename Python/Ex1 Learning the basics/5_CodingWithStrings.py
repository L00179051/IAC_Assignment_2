'''
Python script for: Coding with Strings
Date: 13OCT2023
By: Shahanawaz Shaikh
'''

# Coding with Strings
name = "Shahanawaz"
print(name[0:4:1]) #[start:stop:step] - can use to extract characters from the string,0_1_2_3 in array, it stops at 4th one.
print(name[-1:-4:-1]) #Reverse
firstLetters = name[0:2:1]
lastLetter = name[-1:-2:-1]
print(f"The first two letters in the name {name} are {firstLetters} and the Last letter is {lastLetter}")

# String Interpolation
s1 = "Shahanawaz"
print("Hi " + s1)
print("Hi {} from {}, {country}.\nHow are you?".format(s1 + " Shaikh", "Pune", country="India"))

#String Functions
s2 = "   Shahanawaz Shaikh   "
print(s2.upper()+ "\n",s2.lower()+ "\n",s2.strip())
