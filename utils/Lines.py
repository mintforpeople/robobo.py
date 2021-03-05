class Lines:
    """
    Represents a set of straight lines detected by Robobo in a frame.
    
    Attributes:
        - lines (array): Array with n rows and 4 columns, being n the number of lines detected. Each row has the values 'x1', 'y1', 'x2', 'y2', representing the x and y coordinates of the points 1 and 2 that form the detected line. These coordinates takes positive values.
        - id (int): Sequence frame number. Since the camera starts, each frame has a number to be identified. Takes positive values.
    """

    def __init__(self,lines,id):
        self.lines = lines
        self.id=id

    def __str__(self):
        return "Lane, Id:" + str(self.id) + " lines:" + str(self.lines)