# INET4031 Add Users Script

## Program Description

The **INET4031 Add Users Script** automates the process of adding multiple users and assigning them to groups on a Linux system. This script replaces manual use of commands like `useradd`, `passwd`, and `usermod`, streamlining user management.

## Program User Operation

### Overview
This script reads an input file containing user details, processes each line, and executes necessary system commands to add users and assign them to groups.

### Input File Format
The input file should contain lines with the following five fields, separated by colons:
1. **Username**: The user’s username.
2. **Password**: The user’s password.
3. **Last Name**: The user’s last name.
4. **First Name**: The user’s first name.
5. **Groups**: Comma-separated list of groups, or `-` if no groups are needed.

To skip a user, prepend the line with `#`.

### Command Execution
To run the script:
1. Make the script executable: `chmod +x create-users.py`
2. Run the script: `./create-users.py < create-users.input`

The `<` symbol is used to pass the input file to the script.

### "Dry Run"
In dry-run mode, the script simulates user creation without making changes. It prints the commands that would be run and any errors, allowing you to verify the process before making actual changes to the system. The user is prompted at the start to choose dry-run or real execution.

