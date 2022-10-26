import re
from string import ascii_lowercase, ascii_uppercase, digits

STRING = "".join((ascii_uppercase, ascii_lowercase, digits))

PATTERN = r'^[A-Za-z0-9]{1,16}$'
MATCH = re.compile(PATTERN)
