<#
PowerShell script for: Variables
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

# Assigning value to the variable
$Arr1 = 1, 2, "z", "$"
# Get the variable type
$Arr1.GetType()
# Get the value of the variable
$Arr1 

#Clear and Remove the value of the variable
Get-Variable Arr1 | Clear-Variable
Get-Variable Arr1 | Remove-Variable

[int]$Arr1 = 1
$Arr1.GetType()
$Arr1 = "String" #Expected error due to type difference.

[datetime]$d = "01/05/2024"    
$d.GetDateTimeFormats()         # Get list of date time formats available for the variable

# Math
$a = 1
$b = 2
$c = $a + $b
$c 
Write-Output "Total is $c"