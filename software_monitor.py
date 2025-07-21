#!/usr/bin/env python3
import subprocess

banned_apps = ["discord", "steam", "chromium"]

def check_apps():
    for app in banned_apps:
        result = subprocess.run(["which", app], stdout=subprocess.PIPE)
        if result.stdout:
            print(f"⚠️ {app} is installed.")

if __name__ == "__main__":
    check_apps()
