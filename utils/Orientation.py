class Orientation:
    """
    Represents the orientation of the Smartphone.
    
    Attributes:
        - yaw (float): Rotation in degrees around the Z axis. Takes values between -180 and 180. The yaw angle turn is achieved by turning the base with the wheel motors and the PAN motor.
        - pitch (float): Rotation in degrees around the Y axis. Takes values between -180 and 180. The pitch angle turn is achieved by using the TILT motor or moving the robot through a frontally inclined plane.
        - roll (float): Rotation in degrees around the X axis. Takes values between -180 and 180. The turn in the roll angle cannot be achieved by Robobo, but if the surface on which it moves has a lateral inclination, it will change.

        .. image:: _static/orientation.jpg

    """
    
    def __init__(self, yaw, pitch, roll):
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll

    def __str__(self):
        return "Orientation, yaw: " + str(self.yaw)+", pitch: " + str(self.pitch) + ", roll: " + str(self.roll)
