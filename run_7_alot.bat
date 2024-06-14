@echo off
setlocal

for /L %%i in (1,1,7) do (
    start cmd /k "call inputs.bat | node main.js"
    timeout /t 10 /nobreak
)

endlocal
