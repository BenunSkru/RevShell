# Remove Restore Points
vssadmin delete shadows /all /quiet

# Disable System Restore
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore" -Name "RPSessionInterval" -Value 0
