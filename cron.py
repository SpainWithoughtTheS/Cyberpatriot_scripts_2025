#!/usr/bin/env python3
import os

def list_crons():
    os.system("crontab -l")
    os.system("ls /etc/cron*")

if __name__ == "__main__":
    list_crons()
