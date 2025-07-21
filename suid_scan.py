#!/usr/bin/env python3
import os

def find_suid():
    os.system("find / -type f -perm /6000 -exec ls -ld {} +")

if __name__ == "__main__":
    find_suid()
