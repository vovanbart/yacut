import random

from .constants import LINK_LENGTH, STRING
from .models import URL_map


def get_unique_short_id() -> str:
    while True:
        short_url = "".join(random.choices(population=STRING, k=LINK_LENGTH))
        if not check_original(short_url):
            return short_url


def check_original(target: str) -> str:
    obj = URL_map.query.filter_by(short=target).first()
    if obj:
        return obj.original
