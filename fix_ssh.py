#!/usr/bin/env python3
def secure_ssh():
    config_path = "/etc/ssh/sshd_config"
    with open(config_path, "a") as f:
        f.write("\nPermitRootLogin no\nPasswordAuthentication no\n")

if __name__ == "__main__":
    secure_ssh()
