import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # pattern for IP Address check

    # Check if input is a string first
    if not isinstance(ip, str):
        return False
    
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip)
    if not match:
        return False
    
    # Check each octet is within valid range (0-255)
    for octet in match.groups():
        # checks for leading zeros in IP address octets. Ex: 01.20.20.30 is invalid
        if len(octet) > 1 and octet[0] == '0':
            return False
        
        # convert to integer, then check if it is between the valid IP range of 0-255
        num = int(octet)
        if num < 0 or num > 255:
            return False
    return True

if __name__ == "__main__":
    main()