
class Face:
    """
    Represents the face detected by the smartphone front camera

    - posX: Returns the x position in which a face is detected.
    - posY: Returns the y position in which a face is detected.
    - distance: the distance at which the smartphone front camera detects a face.

    """

    def __init__(self,posx, posy, distance):
        self.posx = posx
        self.posy = posy
        self.distance = distance

    def __str__(self):
        return "Face,  x: " +str(self.posx ) +" y: " +str(self.posy ) +" distance: " +str(self.distance)
