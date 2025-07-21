#!/usr/bin/env python3
import os

def change_weak_passwords():
    weak_passwords = ["123456", "password", "admin", "toor", "qwerty"]
    for user in os.popen("cut -d: -f1 /etc/passwd").read().splitlines():
        if user in ["root", "nobody"]:
            continue
        os.system(f"echo '{user}:CyberP@triot2025!' | chpasswd")

if __name__ == "__main__":
    change_weak_passwords()
