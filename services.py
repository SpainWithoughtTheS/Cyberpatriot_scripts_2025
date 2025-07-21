#!/usr/bin/env python3
import subprocess

to_disable = ["avahi-daemon", "cups", "bluetooth"]

for svc in to_disable:
    subprocess.run(["systemctl", "disable", svc], check=False)
    subprocess.run(["systemctl", "stop", svc], check=False)
