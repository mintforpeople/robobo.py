class Lines:
    """
    Represents a detected straight line
    Attributes:
        - lines: array of shape (n, 4) where each row its a line with the values (x1, y1, x2, y2)
        - id: frame number
    """

    def __init__(self,lines,id):
        self.lines = lines
        self.id=id

    def __str__(self):
        return "Lane, Id:" + str(self.id) + " lines:" + str(self.lines)