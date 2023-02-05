@echo off
setlocal ENABLEDELAYEDEXPANSION
echo "run Aggre_11_9.py"
echo.
echo "------------------" >> log.1
echo %date% %time% >> log.1
for /f "usebackq tokens=*" %%i in (`"python .\Aggre_11_9.py 2>&1"`) do (
@set var1=%%i  
echo !var1! 
echo !var1! >> log.1
)