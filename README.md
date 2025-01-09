# AutoDisableHandsFree

**This project automates the disabling of hands-free mode for a specific Bluetooth device when Bluetooth is enabled on a Windows machine.**

**Setup:**

1. Run `config.bat` to create necessary files.
2. Open `device_name.txt` and enter the exact name of the Bluetooth device.

**Functionality:**

* Upon enabling Bluetooth on the Windows machine:
    * The script checks for the specified device.
    * If found, it automatically disables the "Hands-free" and "Headset" telephony profiles.

**Benefits:**

* Prevents unwanted microphone capablities for higher quality listening on wireless headsets.
* Removes constant disabling of headset telephony.

**Note:**

* This script requires Python of 3.10 or later.

**Author:** [ZadeE1]
**Version:** [1.0]
