import platform
import os

print("=== Runner Health Check ===")
print(f"Hostname : {platform.node()}")
print(f"OS       : {platform.system()} {platform.release()}")
print(f"Python   : {platform.python_version()}")
print(f"CPU count: {os.cpu_count()}")
print(f"Load avg : {os.getloadavg()}")
