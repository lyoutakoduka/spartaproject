param([String]$Group)

$Interpreter = "poetry/windows/.venv/Scripts/python.exe"

Function Filter {
    param([String]$Module)
    $Argument = "-m " + $Module
    Start-Process -FilePath $Interpreter -ArgumentList $Argument -NoNewWindow -Wait
}

If($Group -eq "pytest") {
    Filter "pytest"
}

If($Group -eq "isort") {
    Filter "isort . --check-only"
}

If($Group -eq "black") {
    Filter "black . --check"
}

If($Group -eq "flake") {
    Filter "pflake8 ."
}
