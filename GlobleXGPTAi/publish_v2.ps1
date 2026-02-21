# GlobleXGPTAi Update & Publish Script 🚀
# Run this to easily update your library on PyPI

Write-Host "1. Cleaning old builds..." -ForegroundColor Cyan
if (Test-Path "dist") { rm -r dist }

Write-Host "2. Building version 1.0.1..." -ForegroundColor Cyan
python -m build

Write-Host "3. Checking package..." -ForegroundColor Cyan
python -m twine check dist/*

Write-Host "4. Ready to upload! Run this when you are ready:" -ForegroundColor Yellow
Write-Host "python -m twine upload dist/*" -ForegroundColor Green
