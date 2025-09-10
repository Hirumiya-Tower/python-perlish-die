import sys
from typing import NoReturn

def die(message: str) -> NoReturn:
    sys.exit(message)