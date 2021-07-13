
class Face:
    """
    Represents a face detected by Robobo using the front camera of the smartphone.
    
    Attributes:
        - posx (int): The x coordinate of the tap [0..100]. See: :ref:`screen`.
        - posy (int): The y coordinate of the tap [0..100]. See: :ref:`screen`.
        - distance (int): The rounded distance between the eyes of the person, measured in pixels. The values obtained when the person is near the camera are higher than those obtained when the person is far. Takes positive values.

    """

    def __init__(self,posx, posy, distance):
        self.posx = posx
        self.posy = posy
        self.distance = distance

    def __str__(self):
        return "Face,  x: " + str(self.posx ) + " y: " + str(self.posy ) + " distance: " + str(self.distance)
