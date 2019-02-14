

class QRCode():
    """
    Represents a QRCode detected
    """
    def __init__(self, x, y, dist, p1x, p1y, p2x, p2y, p3x, p3y, id):

        self.x = x
        self.y = y
        self.distance = dist

        self.p1 = {"x":p1x,
                    "y":p1y}

        self.p2 = {"x":p2x,
                   "y":p2y}

        self.p3 = {"x":p3x,
                   "y":p3y}

        self.id = id

    def __str__(self):
        return "QR, Id:"+self.id+" x:"+str(self.x)+" y:"+str(self.y)+" distance:"+str(self.distance)
