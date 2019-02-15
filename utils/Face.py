
class Face:
    """
    Represents the last face detected by Robobo (front camera):

    - posX: (int) Returns the x position in which a face is detected.
    - posY: (int) Returns the y position in which a face is detected.
    - distance: (int) the distance at which the SmartPhone front camera detects a face.

    """

    def __init__(self,posx, posy, distance):
        self.posx = posx
        self.posy = posy
        self.distance = distance

    def __str__(self):
        return "Face,  x: " + str(self.posx ) + " y: " + str(self.posy ) + " distance: " + str(self.distance)
