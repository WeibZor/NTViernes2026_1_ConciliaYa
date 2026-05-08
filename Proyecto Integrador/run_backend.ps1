Set-Location -Path "$PSScriptRoot"
python -m pip install -r requirements.txt
uvicorn api:app --reload --port 8000
