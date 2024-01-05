'''
Python script for: Comparison Operators, Logical and Boolean Operators, Coding with Operators
Date: 13OCT2023
By: Shahanawaz Shaikh
'''

# Comparison Operators
v1 = 2
#print(v1 == 2);print(v1 != 2)

#Logical and Boolean Operators
v2 = 2; v3 = 3
#print(v2==2 and v3!=3)

#Coding with Operators exercise
    #Calculate budget and expenditure for this semester
print("Calculating the projected expense for the entire course based on first month expense.")
MonthlyIncome = int(input("Enter monthly income: "))
ExpenseInFirstMonth = int(input("How much did you spend in the first month? "))
EstimatedIncomeForEntireCourse = MonthlyIncome * 9
EstimatedExpenseForEntireCourse = ExpenseInFirstMonth * 9

print(f"Total income in course duration of nine months would be {EstimatedIncomeForEntireCourse} and estimated expense would be {EstimatedExpenseForEntireCourse}")