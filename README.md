# INET4031 Add Users Script

## Program Description
The INET4031 Add Users Script automates the process of adding multiple users and assigning them to groups on a Linux system. This script replaces the manual use of commands like useradd, passwd, and usermod, streamlining user management and reducing the potential for human error.

## Program User Operation

### Overview
This script reads an input file containing user details, processes each line, and executes the necessary system commands to add users and assign them to groups. This removes the need for repetitive, manual user management tasks, enabling quicker user setup.

### Input File Format
The input file should contain lines with the following five fields, separated by colons:

- **Username**: The user's username.
- **Password**: The user's password.
- **Last Name**: The user's last name.
- **First Name**: The user's first name.
- **Groups**: A comma-separated list of groups the user should be added to, or - if no groups are needed.

To skip a user, prepend the line with #.

Command Execution
To run the script:

Make the script executable:
chmod +x create-users.py
