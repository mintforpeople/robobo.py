
class Tap:
    """
    Represents a tap on smartphone screen. Attributes:

    - x: Returns the position x of the tap
    - y: Returns the position y of the tap.

        .. image:: _static/tap_position.jpg

    - zone: Returns the area of the smartphone screen: forehead, eye, right, left, mouth or chin.

        .. image:: _static/tap_areas.jpg
            :scale: 50 %

    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.zone = self.coordsToZone(x,y)

    def coordsToZone (self, x, y):
        """
        Converts the x,y coordinates of the tap into the name of the corresponding area of the smarthphone screen.

        :param x: the x coordinate of the tap
        :param y: the y coordinate of the tap
        :return: (string) One of the following five values: forehead, eye, right, left, mouth or chin.
        """
        if (y == 0) and (x == 0):
            return None
        elif y < 17:
            return "forehead"
        elif self.rangeFun(y, "between", 17, 56) and self.rangeFun(x, "between", 15, 85):
            return 'eye'
        elif self.rangeFun(y, "between", 65, 77) and self.rangeFun(x, "between", 25, 75):
            return "mouth"
        elif self.rangeFun(x, "between", 0, 15):
            return "left"
        elif self.rangeFun(x, "between", 85, 100):
            return "right"
        elif self.rangeFun(y, "between", 77, 100) and self.rangeFun(x, "between", 15, 85):
            return "chin"

    def rangeFun (self, input, type, r1, r2):
        if type == "between":
            if r1 < r2:
                if (input > r1) and (input < r2):
                    return True
                else:
                    return False
            else:
                if (input > r2) and (input < r1):
                    return True
                else:
                    return False
        else:
            if r1 < r2:
                if (input < r1) or (input > r2):
                    return True
                else:
                    return False
            else:
                if (input < r2) or (input > r1):
                    return True
                else:
                    return False

    def __str__(self):
        return "Tap, (x,y): "+ str(self.x) +", " +str(self.y) + ", zone: " + str(self.zone)
