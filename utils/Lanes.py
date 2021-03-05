class LanePro:
    """
    Represents a lane detected by Robobo, formed by two second degree polynomials.
    
    Attributes:
        - coeffs1 (dict): Dictionary with 'a','b' and 'c' (ax^2 + bx +c) coefficients of the left line.
        - coeffs2 (dict): Dictionary with 'a','b' and 'c' (ax^2 + bx +c) coefficients of the right line.
        - minv (array): Transformation matrix to get to the original perspective.
        - id (int): Sequence frame number. Since the camera starts, each frame has a number to be identified. Takes positive values.

    """

    def __init__(self,
                 l1,
                 l2,
                 l3,
                 r1,
                 r2,
                 r3,
                 minv, id):
        self.coeffs1 = {"a": l1,
                        "b": l2,
                        "c": l3}
        self.coeffs2 = {"a": r1,
                        "b": r2,
                        "c": r3}
        self.minv = minv

        self.id = id

    def __str__(self):
        return "Lane, Id: " + str(id) + "coeffs1:" + str(self.coeffs1) + " coeffs2:" + str(
            self.coeffs2) + " minv:" + str(
            self.minv)


class LaneBasic:
    """
    Represents a lane detected by Robobo, formed by two straight lines.
    
    Attributes:
        - coeffs1 (dict): Dictionary with 'a' and 'b' (ax + b) coefficients of the left line.
        - coeffs2 (dict): Dictionary with 'a' and 'b' (ax + b) coefficients of the right line.
        - id (int): Sequence frame number. Since the camera starts, each frame has a number to be identified. Takes positive values.
    """

    def __init__(self,
                 l1,
                 l2,
                 r1,
                 r2, id):
        self.coeffs1 = {"a": l1,
                        "b": l2}
        self.coeffs2 = {"a": r1,
                        "b": r2}

        self.id = id

    def __str__(self):
        return "Lane, Id: " + str(id) + "coeffs1:" + str(self.coeffs1) + " coeffs2:" + str(
            self.coeffs2)
