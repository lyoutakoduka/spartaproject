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

If($Group -eq "isort") {
    Integration "isort . --check-only"
}

If($Group -eq "black") {
    Integration "black . --check"
}

If($Group -eq "flake") {
    Integration "pflake8 ."
}
