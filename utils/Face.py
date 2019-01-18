
class Face:

    def __init__(self,posx, posy, distance):

        self.posx = posx
        self.posy = posy
        self.distance = distance

    def __str__(self):

        return "Face,  x: " +str(self.posx ) +" y: " +str(self.posy ) +" distance: " +str(self.distance)