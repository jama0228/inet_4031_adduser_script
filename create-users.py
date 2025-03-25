#!/usr/bin/python3
# INET4031
# Ahmed Jama
# 03/24
# 03/25

import os  #  lets you have interaction with the operating system (e.g., running system commands).
import re  #  provides support for regular expressions, used to search for patterns in strings.
import sys  #  lets you to access command-line arguments and handle input/output.

def main():
    for line in sys.stdin:
        # This regular expression searches for lines starting with '#' (comments) and skips them.
        match = re.match("^#", line)

        # The line is split into a list using ':' as the delimiter to get user fields (username, password, etc.)
        fields = line.strip().split(':')

        # The IF statement checks if the line is a comment or doesn't contain exactly 5 fields (invalid input).
        # If the condition is true, it skips processing that line.
        if match or len(fields) != 5:
            continue

        # The username, password, and gecos (full name) are extracted from the fields list.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # The groups field is split by commas to create a list of groups the user should belong to.
        groups = fields[4].split(',')

        # Print a message indicating that the account for the user is being created.
        print("==> Creating account for %s..." % (username))

        # Prepare the command to create the user with the specified gecos information, disabling the password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment this line to actually run the command and create the user.
        os.system(cmd)

        # Print a message indicating that the password for the user is being set.
        print("==> Setting the password for %s..." % (username))

        # Prepare the command to set the user's password using echo and passwd commands.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment this line to actually run the command and set the password.
        os.system(cmd)

        for group in groups:
            # The IF statement checks if the group is not '-', which means the user should be assigned to a valid group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Prepare the command to add the user to the specified group.
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Uncomment this line to actually run the command and add the user to the group.
                os.system(cmd)

if __name__ == '__main__':
    main()

