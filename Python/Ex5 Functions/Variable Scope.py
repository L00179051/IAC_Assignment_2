'''
Python script for: Variable Scope
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

string = "Global"

def scopeFunction():
    string = "Within Function"
    def nestedScopeFunction():
        string = "local"
        print(string)
    nestedScopeFunction()
    return string
print(string)
print(scopeFunction())
# If the value is checked again, it has Global value and does not get changed ever though the value of the same variable was overwritten within function.
print(string) 


# Excercise 2 - Error for using prior to declaration
# global globalv1
# globalv1 = 10

# def f1():
#     localv1 = 5
#     print("Inside the function: localv1 =", localv1)
#     print("Inside the function: globalv1 =", globalv1)
#     global globalv1
#     globalv1 = 20
# f1()
# print("Outside the function: globalv1 =", globalv1)