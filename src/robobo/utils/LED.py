from enum import Enum

class LED(Enum):
    """
     This enumeration represents the list of Robobo base's LEDs

        .. image:: _static/leds.jpg
            :scale: 60 %
            :alt: Top view of Robobo. There are five IR sensors forming a pentagon on the frontal part: Front-C on the upper and central part, Front-RR to the left and Front-LL to the right (from the viewer's point of view) of the first one, and finally Front-R on the left and Front-L on the right of the lower part of the pentagon. There are two IR sensors on the rear part: Back-R on the right and Back-L on the left.

    """
    BackR = "Back-R"
    FrontR = "Front-R"
    FrontRE = "Front-RR"
    FrontC = "Front-C"
    FrontL = "Front-L"
    FrontLL = "Front-LL"
    BackL = "Back-L"
    All = "all"
