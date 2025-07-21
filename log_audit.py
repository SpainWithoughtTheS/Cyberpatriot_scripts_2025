#!/usr/bin/env python3
import os

def audit_logs():
    os.system("grep 'Failed password' /var/log/auth.log")
    os.system("grep 'sudo' /var/log/auth.log")

if __name__ == "__main__":
    audit_logs()
