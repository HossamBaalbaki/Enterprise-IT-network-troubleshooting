<#
.SYNOPSIS
Checks disk usage and alerts if free space < 10%
#>

$threshold = 10

$drives = Get-PSDrive -PSProvider FileSystem

foreach ($drive in $drives) {
    $freePercent = ($drive.Free / $drive.Used + $drive.Free) * 100
    if ($freePercent -lt $threshold) {
        Write-Output "ALERT: $($drive.Name) drive free space is below $threshold%!"
    } else {
        Write-Output "$($drive.Name) drive free space is sufficient ($([math]::Round($freePercent,2))%)"
    }
}
