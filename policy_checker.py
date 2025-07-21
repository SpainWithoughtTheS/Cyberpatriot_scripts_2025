#!/usr/bin/env python3
import os

def check_umask():
    with open("/etc/login.defs") as f:
        for line in f:
            if "UMASK" in line:
                print("UMASK line:", line.strip())

if __name__ == "__main__":
    check_umask()
