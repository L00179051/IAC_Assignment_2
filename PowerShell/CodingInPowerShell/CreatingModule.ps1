<#
PowerShell script for: Creating Module
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

$MyModulePath = "C:\Users\$env:USERNAME\Documents\PowerShell\Modules\HelloWorld"

$MyModule = @"
# GetCurrentYear.PSM1
Function Get-CurrentYear {
    $cy = Get-Date | select year ; $cy = $cy.Year ; Write-Output $cy
}
"@

New-Item -Path $MyModulePath -ItemType Directory -Force | Out-Null
$MyModule | Out-File -FilePath $MyModulePath\GetCurrentYear.PSM1
Get-Module -Name GetCurrentYear -ListAvailable