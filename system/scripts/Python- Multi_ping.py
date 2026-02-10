import subprocess
import platform

# List of  IPs
hosts = ["192.168.10.1", "8.8.8.8", "192.168.10.10"]

# Select --OS
param = "-n" if platform.system().lower()=="windows" else "-c"

for host in hosts:
    print(f"Pinging {host}...")
    res = subprocess.run(["ping", param, "2", host], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"{host} is Online\n")
    else:
        print(f"{host} is Offline\n")
