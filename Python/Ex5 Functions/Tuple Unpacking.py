'''
Python script for: Tuple Unpacking
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

def max(list):
    """
    Function to return the most expensive item passed in list.
    """
    maxprice = 0
    maxpriceitem = ""
    for desc, price in list:
        if price > maxprice:
            maxprice = price
            maxpriceitem = desc
    return maxpriceitem, maxprice
itemlist = [("Computer",1000),("Mouse",5),("keyboard",6)]
ExpensiveItem, Price = max(itemlist)
print(f"Most expensive item is {ExpensiveItem} {Price}")