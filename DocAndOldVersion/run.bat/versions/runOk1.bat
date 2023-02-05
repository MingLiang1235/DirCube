@echo off
setlocal ENABLEDELAYEDEXPANSION
echo "run Aggre_11_9.py"
rem set all=
for /f "usebackq tokens=*" %%i in (`"python .\Aggre_11_9.py 2>&1"`) do (
@set var1=%%i
echo !var1!
set var2=!var2! &echo. !var1! >>log.1

)
rem echo !var1!

