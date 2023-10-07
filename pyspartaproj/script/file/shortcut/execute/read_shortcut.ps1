# Create Windows shortcut by PowerShell.

Param([String]$shortcut_path)

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcut_path)

Write-Output $Shortcut.TargetPath