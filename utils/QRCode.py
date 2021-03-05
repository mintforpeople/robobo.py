class QRCode():
    """
    Represents a QRCode detected by Robobo. Definido por tres puntos. Valor cualitativo que sirve para saber si te acercas o te alejas, no la distancia exacta.

    Attributes:
        - x (int): The x coordinate of the center of the QR, measured in pixels from the left side of the screen. Takes positive values.
        - y (int): The y coordinate of the center of the QR, measured in pixels from the upper side of the screen. Takes positive values.
        - distance (int): Approximated distance between Robobo and the QRCode, measured in meters.
        - p1 (dict): Dictionary with 'x' and 'y' coordinates of the first point of interest.
        - p2 (dict): Dictionary with 'x' and 'y' coordinates of the second point of interest.
        - p3 (dict): Dictionary with 'x' and 'y' coordinates of the third point of interest.
        - id (int): QRCode identifier.
    """

    def __init__(self, x, y, dist, p1x, p1y, p2x, p2y, p3x, p3y, id):
        self.x = x
        self.y = y
        self.distance = dist

        self.p1 = {"x": p1x,
                   "y": p1y}

        self.p2 = {"x": p2x,
                   "y": p2y}

        self.p3 = {"x": p3x,
                   "y": p3y}

        self.id = id

    def __str__(self):
        return "QR, Id:" + self.id + " x:" + str(self.x) + " y:" + str(self.y) + " distance:" + str(self.distance)
