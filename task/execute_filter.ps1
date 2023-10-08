param([String]$Group)

$Interpreter = "poetry/windows/.venv/Scripts/"

Function ExecuteFilter {
    param([String]$Module, [String]$Argument)

    $Executable = $Interpreter + $Module

    Start-Process `
        -FilePath $Executable -ArgumentList $Argument -NoNewWindow -Wait
}

If($Group -eq "isort") {
    ExecuteFilter "isort.exe" "--check-only ."
}

If($Group -eq "black") {
    ExecuteFilter "black.exe" "--check ."
}

If($Group -eq "flake") {
    ExecuteFilter "pflake8.exe" "."
}

If($Group -eq "pytest") {
    ExecuteFilter "python.exe" "-m pytest"
}
