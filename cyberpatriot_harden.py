#!/usr/bin/env python3
import subprocess
import datetime
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)
log_file = f"logs/hardening_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def log(msg):
    with open(log_file, "a") as f:
        f.write(msg + "\n")
    print(msg)

# List of all hardening and audit scripts
scripts = [
    "update.py",
    "passwordchanger.py",
    "account_lockout.py",
    "user_mangment.py",
    "package_audit_new.py",
    "network.py",
    "null.py",
    "fix_ssh.py",
    "cron.py",
    "services.py",
    "log_audit.py",
    "policy_checker.py",
    "rootkit_scan.py",
    "suid_scan.py",
    "integrity_check.py",
    "cleanup.py",
    "forensics_capture.py",
    "software_monitor.py"
]

log("🛡️ Starting CyberPatriot Hardening Toolkit")
log("🗂️ Logging to: " + log_file)

for script in scripts:
    log(f"\n▶️ Running {script}...")
    try:
        output = subprocess.check_output(["python3", script], stderr=subprocess.STDOUT)
        log(output.decode())
    except subprocess.CalledProcessError as e:
        log(f"❌ ERROR: {script} failed with exit code {e.returncode}")
        log(e.output.decode())

log("\n✅ All scripts executed.")
