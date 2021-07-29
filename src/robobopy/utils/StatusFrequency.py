from enum import Enum


class StatusFrequency(Enum):
    """
    This enumeration lists the possible values for setting the frequency of the status messages coming from the robot.
    """
    Low = "LOW"
    Normal = "NORMAL"
    High = "HIGH"
    Max = "MAX"

