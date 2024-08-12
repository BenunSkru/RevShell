# Disable specific processes
$processes = @("processname1", "processname2")
foreach ($process in $processes) {
    Get-Process $process -ErrorAction SilentlyContinue | Stop-Process -Force
}

# Disable specific services
$services = @("ServiceName1", "ServiceName2")
foreach ($service in $services) {
    Stop-Service -Name $service -Force
    Set-Service -Name $service -StartupType Disabled
}
