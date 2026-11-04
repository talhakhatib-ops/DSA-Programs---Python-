# Program to validate an IPv4 or IPv6 address

import ipaddress

address = input("Enter an IP address: ").strip()

try:
    parsed_address = ipaddress.ip_address(address)
    print("Valid", parsed_address.version, "address:", parsed_address)
except ValueError:
    print("Invalid IP address.")
