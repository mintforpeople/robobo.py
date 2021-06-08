from enum import Enum


class BlobColor(Enum):
    """
    This enumeration represents the list of colors Robobo can detect
    """

    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    CUSTOM = 'custom'
