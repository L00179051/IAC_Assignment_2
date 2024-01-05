<#
PowerShell script for: Desired State Configuration
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

configuration EnsureFileExists {
    param (
        [Parameter(Mandatory=$true)]
        [String]$FilePath
    )

    Node $env:COMPUTERNAME {
        File FileEnsureExists {
            DestinationPath = $FilePath
            Contents = "This is some content."
            Ensure = "Present"
        }
    }
}

# Example usage
EnsureFileExists -FilePath "C:users\shahanawaz\desktop\PowerShell\CheckFile.txt"


# Applying the configuration
Start-DscConfiguration -Path C"C:users\shahanawaz\desktop\PowerShell\CheckFile.txt" -Verbose -Wait -Force

# Test DSC Configuration
Get-DscConfiguration

# Removing configuration
$Session = New-CimSession -ComputerName "localhost"
Remove-DscConfigurationDocument -Stage Current -CimSession $Session