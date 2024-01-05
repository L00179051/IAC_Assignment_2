'''
Python script for: Detect Working Directory
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

import os,platform

current_working_directory = None #Global variable

def detect_os() -> str: # Returns output in String type
    return platform.system()

def current_directory() -> str:
    return os.getcwd()

myos = detect_os()
print(myos)
myos = myos.lower()
if myos == "windows": print(f"You are currently using Windows Operating System, the best of all OS")
else: print(f"Not a Windows computer. Microsoft recomends to use a Windows Operating System.") 

# sys.exit() - This does not seem to work, even tried systemexit()