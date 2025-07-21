#!/usr/bin/env python3
import hashlib
import os

critical_files = ["/bin/bash", "/usr/bin/sudo", "/etc/passwd"]

def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

if __name__ == "__main__":
    for f in critical_files:
        print(f"{f}: {hash_file(f)}")
