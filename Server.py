# Final Automation Project
# Jarre' Owens
# CNE 335 Fall

import os

class Server:
#   """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip):
# TODO -
        self.server_ip = server_ip

# pings the server to verify connectivity
    def ping(self):
# TODO - Use os module to ping the server
#https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
#https://docs.python.org/3/library/os.html
        ping_command = f"ping -n 5 {self.server_ip}"
        ping_data = os.popen(ping_command).read()
        print(ping_data)

