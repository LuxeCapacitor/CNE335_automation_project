# Final Automation Project
# Jarre' Owens
# CNE 335 Fall

import os
import paramiko


class Server:

    #   """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip, username, key, update_cmd):
        # TODO -
        self.server_ip = server_ip
        self.username = username
        self.key = key
        self.update_cmd = update_cmd
    # pings the server to verify connectivity

    def ping(self):

        # TODO - Use os module to ping the server
        # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
        # https://docs.python.org/3/library/os.html
        ping_command = f"ping -n 5 {self.server_ip}"
        ping_data = os.popen(ping_command).read()
        print(ping_data)

    def update_server(self):
        # https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        rsa_key = paramiko.RSAKey.from_private_key(self.key)
        ssh.connect(hostname=self.server_ip, username=self.username, pkey=rsa_key)

        stdin, stdout, stderr = ssh.exec_command(self.update_cmd)
        for line in stdout.read().splitlines():
            print(line)

        # Close SSH connection
        ssh.close()
