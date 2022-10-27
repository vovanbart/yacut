import re
from string import ascii_lowercase, ascii_uppercase, digits

STRING = "".join((ascii_uppercase, ascii_lowercase, digits))

PATTERN_LINK = r'^[A-Za-z0-9]{1,16}$'
MATCH_LINK = re.compile(PATTERN_LINK)
PATTERN_LINK1 = r'[A-Za-z0-9]+'
LINK_LENGTH = 6
