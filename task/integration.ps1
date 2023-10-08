param([String]$Group)

$Interpreter = "poetry/windows/.venv/Scripts/python.exe"

Function Integration {
    param([String]$Module)
    $Argument = "-m " + $Module
    Start-Process -FilePath $Interpreter -ArgumentList $Argument -NoNewWindow -Wait
}

If($Group -eq "pytest") {
    Integration "pytest"
}
