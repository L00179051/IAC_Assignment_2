<#
PowerShell script for: Conditional Breaching
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

# using If and else statement
$a = 3
$b = 5
if ($a -lt $b){
    Write-Output "Value of variable 'a' is less than that of 'b'"
} elseif ($a -gt $b) {
    Write-Output "Value of variable 'a' is greater than that of 'b'"
} else {
    Write-Output "Value of variable 'a' is equal to the value of 'b'"
}

$day = 3

switch ($day) {
    0 { $result = 'Sunday'}
    1 { $result = 'Monday'}
    2 { $result = 'Tuesday'}
    3 { $result = 'Wednesday'}
    4 { $result = 'Thursday'}
    5 { $result = 'Friday'}
    6 { $result = 'Saturday'}
}

$result