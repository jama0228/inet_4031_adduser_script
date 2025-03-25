#!/usr/bin/python3

# INET4031
# Your Name
# Date Created
# Date Last Modified

import os
import re
import sys

def main():
    # Prompt the user to decide if they want to run the script in dry-run mode
    dry_run = input("Would you like to run the script in dry-run mode? (Y/N): ").strip().lower()
    if dry_run not in ['y', 'n']:
        print("Invalid input, defaulting to 'N'.")
        dry_run = 'n'

    for line in sys.stdin:
        match = re.match("^#", line)

        # Split the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

        # Skip lines that do not have exactly 5 fields or are commented out
        if match or len(fields) != 5:
            if dry_run == 'y':
                print(f"==> Skipping line (incorrect format or commented): {line.strip()}")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # If dry-run mode, print the actions that would happen
        if dry_run == 'y':
            print(f"==> Dry-run: Creating account for {username}...")
            print(f"==> Dry-run: Setting the password for {username}...")
            for group in groups:
                if group != '-':
                    print(f"==> Dry-run: Assigning {username} to the {group} group...")
        else:
            # If not in dry-run mode, execute the commands
            print(f"==> Creating account for {username}...")
            cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
            # Uncomment to execute: os.system(cmd)

            print(f"==> Setting the password for {username}...")
            cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
            # Uncomment to execute: os.system(cmd)

            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = "/usr/sbin/adduser %s %s" % (username, group)
                    # Uncomment to execute: os.system(cmd)

if __name__ == '__main__':
    main()
