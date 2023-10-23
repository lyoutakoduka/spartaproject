Param([String]$text_left, [String]$text_right)

if ($text_left -ceq $text_right)
{
    if ([System.IO.File]::Exists($text_left))
    {
        Write-Output $text_left
    }
}
