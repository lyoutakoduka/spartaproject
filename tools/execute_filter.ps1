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
ElseIf ($Group -eq "black") {
    ExecuteFilter "black.exe" "--check ."
}
ElseIf ($Group -eq "flake") {
    ExecuteFilter "pflake8.exe" "."
}
ElseIf ($Group -eq "mypy") {
    ExecuteFilter "mypy.exe" "."
}
ElseIf ($Group -eq "pytest") {
    ExecuteFilter "python.exe" "-m pytest"
}
