#!/usr/bin/env python3
import subprocess

def update_system():
    subprocess.run(["apt", "update"], check=True)
    subprocess.run(["apt", "upgrade", "-y"], check=True)

if __name__ == "__main__":
    update_system()
