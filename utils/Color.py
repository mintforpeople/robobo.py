from enum import Enum


class Color(Enum):
    """
    Represents the list of colors Robobo's LEDs can show.
    """
    OFF = 'off'
    WHITE = 'white'
    RED = 'red'
    BLUE = 'blue'
    CYAN = 'cyan'
    MAGENTA = 'magenta'
    YELLOW = 'yellow'
    GREEN = 'green'
    ORANGE = 'orange'
