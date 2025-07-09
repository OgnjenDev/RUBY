# kernel.py — Ruby OS Boot Sequence

import os
import time

OS_NAME = "Ruby OS"
OS_VERSION = "1.3.4"
OS_AUTHOR = "Ognjen Đokić"

def boot():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{OS_NAME} v{OS_VERSION} by {OS_AUTHOR}")
    print("=" * 30)
    time.sleep(0.8)
    print("[ OK ] Loading kernel...")
    time.sleep(0.8)
    print("[ OK ] Initializing drivers...")
    time.sleep(0.8)
    print("[ OK ] Starting services...")
    time.sleep(0.8)
    print("[ OK ] Finalizing setup...")
    time.sleep(0.8)
    print("\nSystem ready!\n")
    time.sleep(0.5)

if __name__ == "__main__":
    boot()