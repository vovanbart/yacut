import re
from string import ascii_lowercase, ascii_uppercase, digits

STRING = "".join((ascii_uppercase, ascii_lowercase, digits))

PATTERN_LINK = r'^[A-Za-z0-9]{1,16}$'
MATCH_LINK = re.compile(PATTERN_LINK)
LINK_LENGTH = 6
GET = 'GET'
POST = 'POST'
