#!/usr/bin/env python3
import os

def snapshot():
    os.system("ps aux > snapshot_processes.txt")
    os.system("who > snapshot_users.txt")
    os.system("ss -tulnp > snapshot_ports.txt")

if __name__ == "__main__":
    snapshot()
