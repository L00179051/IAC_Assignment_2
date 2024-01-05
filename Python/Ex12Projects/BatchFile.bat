:: This is the Batch file for creating the required folder structure
:: By: Shahanawaz Shaikh
:: Initial file: 23Nov2023
:: Filename: CreateFolderStructure.bat

@echo off
cls
title Create Folder Structure
echo "*******************************************"
echo Below folders will be created if they do not exist:
echo Documentation
echo Examples
echo Source
echo Tests
echo "*******************************************"

::SET folderPath=G:\Assignments\Infrastructure as Code\IAC Assignment 1\L00179051\Practice\
::The above path did not work during execution as it had a space in folder name.


SET folderPath=%cd% 
:: The above command gets the current path of the directory where batch file is executed
:: Below folder names are saved in variables
SET f1=Documentation
SET f2=Examples
SET f3=Source
SET f4=Tests

::echo Filepath %folderPath%%f1% - Need to run this commented command to check the value in the variables.

if not exist %folderPath%\%f1% (
    mkdir "Documentation"
    echo Folder - "Documentation" has been created
) else (
    echo Folder - "Documentation" already exists
    )

if not exist %folderPath%\%f2% (
    mkdir "Examples"
    echo Folder - "Examples" has been created
) else (
    echo Folder - "Examples" already exists
    )

if not exist %folderPath%\%f3% (
    mkdir "Source"
    echo Folder - "Source" has been created
) else (
    echo Folder - "Source" already exists
    )

if not exist %folderPath%\%f4% (
    mkdir "Tests"
    echo Folder - "Tests" has been created
) else (
    echo Folder - "Tests" already exists
    )

pause