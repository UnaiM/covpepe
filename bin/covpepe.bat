@echo off

call "%~dp0..\venv\Scripts\activate"

python "%~dp0..\src\covpepe.py" %* || pause
