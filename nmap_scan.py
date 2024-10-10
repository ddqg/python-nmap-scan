#!/usr/bin/python3

import nmap

ascii_art = """
⠀⠀⠀⡇⡇⠀ ⠀⠀⡇
⠀⠀⠀⡆⡇⠀ ⠀⠀⡇⡄
⠀⠀⠀⠁⡇⠇⠀⡂⡇⡇  wkm
⠀⠀⠀⡇⣇⠃⠀⣇⣁⡇
⠀⠀⠀⣧⣿⣷ ⣾⣿⡷
⠀⠀⠀⠘⣿⣿ ⣿⡏
⠀⠀⠀⠀⢸⣿ ⣿⡇⠀⣀
⠀⠀⠀⠀⣸⣿ ⣿⡷⠛⣿
⠀⢀⠀⠀⣿⣿⡿⣷⣶⣿⣤⡴⠞⢿
⠀⢸⠀⠀⣿⣿⣿⠰⢹⡿⢿⣿⣤⠟
⠀⠘⢸⠀⣿⣿⣿⣏⣽⣄⣃⣿⡇
⠀⢸⢨⢠⣼⣿⣿⣿⣿⣿⣿⡟
⠀⠘⣠⡌⢿⣿⣿⣿⣿⣿⣄⠀
⠀⢸⣿⡿⢸⣿⣿⣿⣿⣿⣿⣧
⠀⠀⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⣿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⠀⠻⠿⠟⠛⠻⠿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠈⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣄⠀⠀⠀⢀⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣶⣶⠿⠋
"""

print(ascii_art)

scanner = nmap.PortScanner()

ip = str(input("Target IP: "))

scan_args = '-A -T4 -vv'

print(f"Starting Nmap scan on {ip} for ports 1 to 65535...")
scanner.scan(ip, '1-65535', arguments=scan_args)

for host in scanner.all_hosts():
    print(f"Host result: {host}")
    print(f"Host state: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")

        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"Port: {port}\t State: {scanner[host][proto][port]['state']}")
            if 'product' in scanner[host][proto][port]:
                print(f"Service: {scanner[host][proto][port]['product']}")
            if 'version' in scanner[host][proto][port]:
                print(f"Version: {scanner[host][proto][port]['version']}")
