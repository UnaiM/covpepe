@echo off

python3 -m venv "%~dp0../venv"
call "%~dp0../venv/Scripts/activate"
pip install pyperclip

for /f USEBACKQ %%f in (`powershell "[Environment]::GetFolderPath('SendTo')"`) DO set "sendto=%%f"
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%sendto%\covpepe.lnk');$s.TargetPath='%~dp0..\bin\covpepe.bat';$s.Save()"

reg add HKCU\Software\Classes\directory\Background\shell\pasvtete\command /ve /d "%~dp0..\bin\pasvtete %%*"

pause
