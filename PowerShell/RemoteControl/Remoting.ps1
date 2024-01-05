<#
PowerShell script for: Initial Setup
Date: 05JAN2024
By: Shahanawaz Shaikh
#>

# Performing actions remotely
$Remote_Server = "WIN2016DC-S05"
Enter-PSSession $Remote_Server
    Get-Service *dhcp* | Restart-Service
Exit-PSSession


# Promoting server as a domain controller for a new forest
Install-WindowsFeature -name AD-Domain-Services –IncludeManagementTools
Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainName "idealsolutions.ie" `
-DomainNetbiosName "idealsolutions" `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
Shutdown /r /t 0


$SERVERNAME = "WIN2016DC-S05"
$FOREST = "idealsolutions.ie"
$DNSNAME = $SERVERNAME + "." + $FOREST

# Set the IP address for the DC
Rename-Computer -NewName $SERVERNAME
Get-NetIPAddress
New-NetIPAddress -InterfaceIndex 16 -IPAddress 71.27.6.11 -PrefixLength 24 -DefaultGateway 71.27.6.20
Restart-Computer

# Configure AD, DNS
Install-ADDSForest -DomainName $FOREST
Install-WindowsFeature DHCP -IncludeManagementTools
# Configure DHCP, add a single scope
Add-DhcpServerInDC -DnsName $DNSNAME -IPAddress 71.27.6.11
Add-DhcpServerv4Scope -Name InfraServers -StartRange 71.27.6.150 -EndRange 71.27.6.199 -SubnetMask 255.255.255.0
