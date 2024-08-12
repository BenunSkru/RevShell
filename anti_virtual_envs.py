import os
import sys

def detect_virtual_environment():
    if os.path.exists('/.dockerenv'):
        return True
    if any(x in os.getenv('PATH', '') for x in ('VirtualBox', 'VMware')):
        return True
    return False

def detect_debugger():
    return sys.gettrace() is not None

if detect_virtual_environment() or detect_debugger():
    print("Virtual environment or debugger detected. Exiting...")
    sys.exit(1)
