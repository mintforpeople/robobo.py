

class Acceleration:
    """
    Represents the current acceleration of the SmartPhone (x, y, z)
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Acceleration, x:"+ str(self.x)+", y:"+str(self.y) + ", z: " + str(self.z)
