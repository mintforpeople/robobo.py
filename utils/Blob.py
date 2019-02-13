

class Blob:
    """
    Represents a blob detected:
        * color: (string) The color of the blob
        * posx: (int) The x coordinate of the center of the blob area
        * posy: (int) The y coordinate of the center of the blob area
        * size: (int) The area of the blob measured in pixels.
    """
    def __init__(self, color, posx, posy, size):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.size = size

    def __str__(self):
        return self.color+" blob,  x:"+str(self.posx)+" y:"+str(self.posy)+" size:"+str(self.size)

