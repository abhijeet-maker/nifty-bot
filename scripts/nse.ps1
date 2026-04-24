param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$Root = Resolve-Path "$PSScriptRoot\.."
$Python = Join-Path $Root ".venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    $Python = "python"
}

$Script = Join-Path $PSScriptRoot "lib\nse_data.py"
& $Python $Script @Args
exit $LASTEXITCODE
