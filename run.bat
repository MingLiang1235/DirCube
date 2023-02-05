@echo off
setlocal ENABLEDELAYEDEXPANSION
echo "run Aggre_11_9.py"
set flag=
for /f "usebackq tokens=*" %%i in (`"python .\Aggre_11_9.py 2>&1"`) do (
@set var1=%%i
rem echo !var1!
	 if not defined var1 ( echo "no error") else (
	 	if not defined flag (
	 		echo "has error,see log.1 for detail"
			echo &echo.-------------------------------------- >> log.1
			echo %date% %time% >> log.1
			set flag=1)
	 	set var2=!var2! &echo. !var1! >>log.1)


)