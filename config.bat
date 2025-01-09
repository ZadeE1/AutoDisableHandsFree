@echo off
set "script_dir=%~dp0"
set "run_bat_path=%script_dir%run.bat"


schtasks /Create /TN "Run_main_py_on_Bluetooth_Connect_disable_hands_free" /TR "%run_bat_path%" /ec System /Sc Onevent /Mo "*[System[Provider[@Name='BTHUSB'] and EventID=18]]"
echo Done config, make sure to set a device name in device_name.txt before use