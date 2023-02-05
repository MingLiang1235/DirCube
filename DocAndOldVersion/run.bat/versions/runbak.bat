@echo off
setlocal ENABLEDELAYEDEXPANSION
echo "run Aggre_11_9.py"
set all=
for /f "usebackq tokens=*" %%i in (`"python .\Aggre_11_9.py 2>&1"`) do (
@set var1=!var1!&echo.&echo.%%i >> log.1
echo !var1!
)
rem echo !var1!

