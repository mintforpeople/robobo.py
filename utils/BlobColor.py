from enum import Enum


class BlobColor(Enum):
    """
    Represents the list of colors Robobo can detect
    """

    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    CUSTOM = 'custom'
