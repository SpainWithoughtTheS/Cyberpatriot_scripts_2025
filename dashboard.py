#!/usr/bin/env python3
import curses
import subprocess

# Define the script list (make sure these match your actual filenames)
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

def run_script(index):
    try:
        subprocess.run(["python3", scripts[index]])
    except Exception as e:
        print(f"Error running {scripts[index]}: {e}")

def dashboard(stdscr):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "🛡️ CyberPatriot Hardening Dashboard", curses.A_BOLD)

        for i, script in enumerate(scripts):
            if i == current_row:
                stdscr.addstr(i + 2, 4, f"> {script}", curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 6, script)

        stdscr.addstr(len(scripts) + 3, 4, "[ENTER] Run  |  [↑/↓] Navigate  |  [Q] Quit")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q") or key == ord("Q"):
            break
        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(scripts) - 1:
            current_row += 1
        elif key == ord("\n"):
            stdscr.clear()
            stdscr.addstr(0, 2, f"▶ Running {scripts[current_row]}...", curses.A_BOLD)
            stdscr.refresh()
            run_script(current_row)
            stdscr.addstr(2, 2, "✔ Done. Press any key to return.")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(dashboard)
