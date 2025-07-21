#!/usr/bin/env python3
import subprocess

def scan_rootkits():
    subprocess.run(["chkrootkit"], check=False)

if __name__ == "__main__":
    scan_rootkits()
