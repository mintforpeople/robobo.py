

class Orientation:
    """
    Represents the current orientation of the smartphone. Attributes: yaw, pitch and roll.

        .. image:: _static/orientation.jpg

    """
    
    def __init__(self, yaw, pitch, roll):
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll

    def __str__(self):
        return "Orientation, yaw: " + str(self.yaw)+", pitch: " + str(self.pitch) + ", roll: " + str(self.roll)
