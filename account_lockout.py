#!/usr/bin/env python3
def enforce_lockout():
    pam_file = "/etc/pam.d/common-auth"
    with open(pam_file, "a") as f:
        f.write("\nauth required pam_tally2.so deny=3 onerr=fail unlock_time=900\n")

if __name__ == "__main__":
    enforce_lockout()
