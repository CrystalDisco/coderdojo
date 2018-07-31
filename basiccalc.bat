@echo off
title Basic Calculator

:calculate
cls
echo Enter your basic mathematic equation here!
set /p equation=Equation: 
set /a result = %equation%
echo The result is %result%
pause
goto calculate
