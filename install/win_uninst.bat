@echo off

rd /s /q "%~dp0../venv"

for /f USEBACKQ %%f in (`powershell "[Environment]::GetFolderPath('SendTo')"`) DO set "sendto=%%f"
del "%sendto%\covpepe.lnk"

reg delete HKCU\Software\Classes\directory\Background\shell\pasvtete /f

pause
