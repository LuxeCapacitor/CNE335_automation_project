# Final Automation Project
# Jarre' Owens
# CNE 335 Fall

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Jarre' Owens")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = '3.145.34.41'
    username = 'ubuntu'
    key = r'C:\users\owens\.ssh\AWSPrivateKey.ppk'
    update_cmd = 'sudo apt update && sudo apt upgrade -y'
    # TODO - Call Ping method and print the results
    my_server = Server(server_ip, username, key, update_cmd)
    update_info = my_server.update_cmd
    print(my_server.ping())
    print('\n' * 2)
    print('Update Results:')
    print('\n' * 2)
    print(update_info)


