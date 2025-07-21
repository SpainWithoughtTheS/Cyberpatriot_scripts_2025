#!/usr/bin/env python3
import subprocess

def add_and_secure_users():
    subprocess.run(["usermod", "-aG", "sudo", "cyberpatriot"])
    subprocess.run(["passwd", "-l", "guest"], check=False)

if __name__ == "__main__":
    add_and_secure_users()
