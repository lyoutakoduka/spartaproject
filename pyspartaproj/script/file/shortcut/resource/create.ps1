# Create Windows shortcut by PowerShell.

Param([String]$shortcut_target, [String]$shortcut_path)

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcut_path)
$Shortcut.TargetPath = $shortcut_target
$Shortcut.Save()
