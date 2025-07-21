#!/usr/bin/env python3
import os

def clean():
    os.system("apt autoremove -y")
    os.system("rm -rf /tmp/* /var/tmp/*")

if __name__ == "__main__":
    clean()
