import subprocess
import os

# List of Bluetooth device names to monitor
device_list = ["Earmuffs"]

# Path to the bin folder relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
bin_path = os.path.join(script_dir, "bin")

# Paths to btcom and btdiscovery executables
btcom_path = os.path.join(bin_path, "btcom.exe")
btdiscovery_path = os.path.join(bin_path, "btdiscovery.exe")

# Function to check if a device is connected
def is_device_connected(device_name):
    try:
        # Run the btdiscovery command and capture output
        result = subprocess.run(
            [btdiscovery_path, "-n", device_name, "-d%c%"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # Debug: Print raw output from the command
        print(f"[DEBUG] Output for {device_name}: {result.stdout.strip()}")
        # Return True if the output contains "Yes"
        return "Yes" in result.stdout
    except Exception as e:
        print(f"[ERROR] Failed to check connection for {device_name}: {e}")
        return False

# Function to disable handsfree telephony
def disable_handsfree(device_name):
    try:
        # Run the btcom command
        result = subprocess.run(
            [btcom_path, "-r", "-n", device_name, "-s111E"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # Debug: Print output of the btcom command
        print(f"[DEBUG] btcom output for {device_name}: {result.stdout.strip()}")
        if result.returncode == 0:
            print(f"[INFO] Successfully disabled handsfree telephony for {device_name}")
        else:
            print(f"[ERROR] Failed to disable handsfree telephony for {device_name}: {result.stderr.strip()}")
    except Exception as e:
        print(f"[ERROR] Failed to run btcom for {device_name}: {e}")

# Check devices and disable handsfree if necessary
def check_and_disable():
    print("[INFO] Checking devices...")
    for device in device_list:
        if is_device_connected(device):
            print(f"[INFO] {device} is connected. Disabling handsfree telephony...")
            disable_handsfree(device)
        else:
            print(f"[INFO] {device} is not connected.")
            check_and_disable()

# Call the function to perform the check
check_and_disable()