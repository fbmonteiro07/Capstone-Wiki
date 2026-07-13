@echo off
rem Rebuilds data.js from the Sensor Tower base workbook (path in source_path.txt)
cd /d %~dp0
py build_data.py
pause
