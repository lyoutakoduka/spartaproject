param([String]$Group)

$Interpreter = "poetry/windows/.venv/Scripts/python.exe"

Function ExecuteFilter {
    param([String]$Module)
    $Argument = "-m " + $Module
    Start-Process -FilePath $Interpreter -ArgumentList $Argument -NoNewWindow -Wait
}

If($Group -eq "isort") {
    ExecuteFilter "isort . --check-only"
}

If($Group -eq "black") {
    ExecuteFilter "black . --check"
}

If($Group -eq "flake") {
    ExecuteFilter "pflake8 ."
}

If($Group -eq "pytest") {
    ExecuteFilter "pytest"
}
