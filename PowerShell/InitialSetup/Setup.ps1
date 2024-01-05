<#
PowerShell script for: Initial Setup
Date: 05JAN2024
By: Shahanawaz Shaikh
#>



# To fetch the current PS Version value
$PSVersiontable
# Set an execution policy to remotesigned or unrestricted, may require PowerShell to launched as an admin
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force
# Install Nuget as a package provider
Install-PackageProvider Nuget -MinimumVersion 2.8.5.201 -Force | Out-Null
# Install the module
Install-Module -Name PowerShellGet -Force -AllowClobber
# Create a script directory
New-Item -ItemType directory -Name PowerShell

