import os
import sys

def setup_windows_console():
    if os.name == 'nt':
        os.system('title DDoS Protection Server')
        os.system('color 0A')  # Green on black

def validate_port(port):
    try:
        port = int(port)
        if 1 <= port <= 65535:
            return port
    except ValueError:
        return None