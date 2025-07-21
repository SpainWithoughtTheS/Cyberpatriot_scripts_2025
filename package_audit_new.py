#!/usr/bin/env python3
import subprocess

banned = ["netcat", "nmap", "hydra", "john", "wireshark"]

for pkg in banned:
    subprocess.run(["apt", "remove", "-y", pkg], check=False)
