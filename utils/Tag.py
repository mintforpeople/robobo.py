class Tag:
    """
    Represents a detected Aruco Tag
    Attributes:
        - cor1: Dictionary with 'x' and 'y' coordinates of the first corner.
        - cor2: Dictionary with 'x' and 'y' coordinates of the second corner.
        - cor3: Dictionary with 'x' and 'y' coordinates of the third corner.
        - cor4: Dictionary with 'x' and 'y' coordinates of the fourth corner.
        - tvecs: Dictionary with the 'x', 'y' and 'z' components of the translation vector.
        - tvecs: Dictionary with the 'x', 'y' and 'z' components of the rotation vector.
        - id: ArUco identifier.
    """

    def __init__(self, cor1x, cor1y, cor2x, cor2y, cor3x, cor3y, cor4x, cor4y, rvec_0, rvec_1, rvec_2, tvec_0, tvec_1,
                 tvec_2, id):
        self.cor1 = {"x": cor1x,
                     "y": cor1y}

        self.cor2 = {"x": cor2x,
                     "y": cor2y}

        self.cor3 = {"x": cor3x,
                     "y": cor3y}

        self.cor4 = {"x": cor4x,
                     "y": cor4y}

        self.tvecs = {"x": tvec_0,
                      "y": tvec_1,
                      "z": tvec_2}

        self.rvecs = {"x": rvec_0,
                      "y": rvec_1,
                      "z": rvec_2}

        self.id = id

    def __str__(self):
        return "Aruco, Id:" + self.id + " cor1:" + str(self.cor1) + " cor2:" + str(self.cor2) + " cor3:" + str(
            self.cor3) + " cor4:" + str(self.cor4) + " tvecs:" + str(self.tvecs) + " rvecs:" + str(self.rvecs)
