from enum import Enum

class IR(Enum):
    """
    This enumeration represents the list of Robobo base's IR

        .. image:: _static/irs.jpg
            :alt: One image from Robobo frontal part, showing five IR sensors, named from left to right: Front-RR, Front-R, Front-C, Front-L and Front-LL. Another image from Robobo rear part, showing three IR sensors, named from left to right: Back-L, Back-C, Back-R.

    """
    BackR = "Back-R"
    BackC = "Back-C"
    FrontR = "Front-R"
    FrontRR = "Front-RR"
    FrontC = "Front-C"
    FrontL = "Front-L"
    FrontLL = "Front-LL"
    BackL = "Back-L"
