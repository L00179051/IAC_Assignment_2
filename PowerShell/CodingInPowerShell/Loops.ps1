<#
PowerShell script for: Loops
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

# Using for loop
for ($i = 0; $i -lt 3; $i++) {
    Write-Output "Value of i is $i"
}

# Using foreach
$s = Get-Service | select -First 5 | select DisplayName # Selects only first 5 results
$s = $s.DisplayName
$s |  foreach {Write-Output "Service name is $_"}

# Using While
while ($i -lt 6) {
    $i++
    Write-Host $i
}

# Do Until - quite similar to while
do {
    $i ; $i++
} until ($i -lt 10)