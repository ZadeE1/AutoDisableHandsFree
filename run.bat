@echo off
set "script_dir=%~dp0"
set "run_py_path=%script_dir%main.py"


python %run_py_path%
notepad