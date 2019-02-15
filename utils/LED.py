from enum import Enum

class LED(Enum):
    """
     Represents the list of Robobo base's LEDs

        .. image:: _static/leds.jpg
            :scale: 60 %

    """
    BackR = "Back-R"
    FrontR = "Front-R"
    FrontRE = "Front-RR"
    FrontC = "Front-C"
    FrontL = "Front-L"
    FrontLL = "Front-LL"
    BackL = "Back-L"
    All = "all"
