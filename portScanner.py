#!/usr/bin/python

"""
A simple TCP port scanner.
By: Michael Cosmadelis
"""

import socket
import sys

def main():
    # prompts the user for input
    host = raw_input("Enter host IP to scan: ")
    hostip = socket.gethostbyname(host)
    # checks the validity of the IP inputted
    if len(host.split(".")) != 4:
        print("Target host must be a valid IPv4 address")
        return 1
    print "=" * 25
    print("Scanning " + host + " please wait...")

    try:
        # performs a TCP connection on each port
        for port in range(1, 1000):
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.settimeout(2)
            result = sckt.connect_ex((hostip, port))
            # if connection is successful that port is open
            if result == 0:
                print("Port {} is open.").format(port)
            sckt.close()
    except KeyboardInterrupt:
        print("Scan stopped.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to host")
        sys.exit()

if __name__ == '__main__':
    sys.exit(main())