"""
Backend module for offering various functions.
"""

import random

def generate() -> int:
    """Generates a random number from 0 to 99.

    Returns:
        Generated number.
    """
    return random.randrange(0, 100)


# TODO(BECATRUE): Change _num to num when saving to a database is implemented.
def save(_num: int, db_name: str) -> bool:
    """Store the number in the database.

    Args:
        _num: Number to store.
        db_name: A string that indicates the name of database.

    Returns:
        True if store succeeds, otherwise False.
    """
    if db_name == "None":
        return False

    return True
