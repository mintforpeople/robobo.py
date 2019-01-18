

class Blob:
    
    def __init__(self, color, posx, posy, size):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.size = size

    def __str__(self):

        return self.color+" blob,  x:"+str(self.posx)+" y:"+str(self.posy)+" size:"+str(self.size)