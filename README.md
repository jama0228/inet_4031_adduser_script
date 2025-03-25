k# INET4031 Add Users Script

## Program Description
The INET4031 Add Users Script automates the process of adding multiple users and assigning them to groups on a Linux system. This script replaces manual use of commands like `useradd`, `passwd`, and `usermod`, streamlining user management.

## Program User Operation

### Overview
This script reads an input file containing user details, processes each line, and executes necessary system commands to add users and assign them to groups.

### Input File Format
The input file should contain lines with the following five fields, separated by colons:

- **Username**: The user’s username.
- **Password**: The user’s password.
- **Last Name**: The user’s last name.
- **First Name**: The user’s first name.
- **Groups**: Comma-separated list of groups, or `-` if no groups are needed.

To skip a user, prepend the line with `#`.

### Command Execution
To run the script:

1. Make the script executable:
   ```bash
   chmod +x create-users.py

