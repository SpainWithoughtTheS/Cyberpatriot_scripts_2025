#!/usr/bin/env python3
def disable_mounts():
    with open("/etc/fstab", "a") as f:
        f.write("\ntmpfs /tmp tmpfs defaults,noexec,nosuid 0 0\n")

if __name__ == "__main__":
    disable_mounts()
