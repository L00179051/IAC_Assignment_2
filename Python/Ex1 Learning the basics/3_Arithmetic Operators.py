'''
Python script for: Arithmetic Operators
Date: 13OCT2023
By: Shahanawaz Shaikh
Reference link: https://johnoraw.gitbook.io/iac-practice/v/pfcs/1.-learning-the-basics/arithmetic-operators
'''

#Precedence
v1 = 4/2 * 2 - (1+2) 
print(v1)

#Mixing types
#v2 = "String1" + 1.5  #TypeError
v2 = "String1"; print(type(v2))
v3 = 1.5; print(type(v3))
print(type(str(v3)))
v4 = v2 + str(v3); print(v4) #Now it works as both variable of same type.

#Modulus and Floor Division
print(5/2);print(5//2) # // is Floor Division so output for 5//2 is 2 and not 2.5

