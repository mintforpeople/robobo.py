

class Acceleration:
    """
    Represents the acceleration of the smartphone.

    Attributes:
        - x (float): acceleration on the X axis (m/s^2).
        - y (float): acceleration on the Y axis (m/s^2).
        - z (float): acceleration on the Z axis (m/s^2).
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Acceleration, x:"+ str(self.x)+", y:"+str(self.y) + ", z: " + str(self.z)
