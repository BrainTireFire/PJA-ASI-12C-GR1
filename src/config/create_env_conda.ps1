$envFile = "environment.yml"

# Check if the environments.yml file exists
if (-not (Test-Path $envFile)) {
    Write-Host "Error: '$envFile' not found."
    exit 1
}

# Get the environment name from the YAML file
$envName = (Get-Content $envFile | Select-String -Pattern 'name:' | ForEach-Object { $_ -replace 'name:','' }).Trim()

# Creating an environment from a YAML file
conda env create -f $envFile

# Activation of the environment
conda activate $envName

Write-Host "The environment '$envName' has been successfully created and activated."
