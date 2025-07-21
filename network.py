#!/usr/bin/env python3
import subprocess

def configure_firewall():
    subprocess.run(["ufw", "default", "deny", "incoming"])
    subprocess.run(["ufw", "default", "allow", "outgoing"])
    subprocess.run(["ufw", "enable"], input=b"y\n")

if __name__ == "__main__":
    configure_firewall()
