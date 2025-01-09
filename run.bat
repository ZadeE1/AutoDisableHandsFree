echo %cwd%
set "script_dir=%~dp0"
cd %script_dir%
set "run_py_path=%script_dir%main.py"


python %run_py_path%
