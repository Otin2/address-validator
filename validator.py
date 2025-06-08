import re

def is_valid_address(address):
    if not isinstance(address, str):
        return False
    pattern = r'^[A-Za-z\s]+\s\d+$'
    return bool(re.match(pattern, address.strip()))