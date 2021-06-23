# This program is designed to modify an existing switch port using designated templates of config.
# It first asks for a switch name to connect to, then a port you want to modify, along with user/pass for the switch.
# Then it displays the current config of the port and asks what template you want to use to modify it.

import paramiko

# Ask for the switch name and set it as the hostname variable.
hostname = input("Enter the switch name: ")
# Ask for the interface name and set it as the interface variable.
interface = input("Enter the interface name: ")
# Ask for the username name and set it as the username variable.
username = input("Enter the username name: ")
# Ask for the password name and set it as the password variable.
password = input("Enter the password name: ")


#Connect to the switch and gather the config
ssh = paramiko.SSHClient()
ssh.connect(hostname,
