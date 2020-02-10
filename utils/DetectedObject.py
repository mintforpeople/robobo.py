class DetectedObject:
    """
    Represents a detected object
    """

    def __init__(self, x, y, width, height, confidence, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.confidence = confidence

    def __str__(self):
        return "DETECTED_OBJECT, Label:" + self.label + \
               " x:" + str(self.x) + \
               " y:" + str(self.y) + \
               " height:" + str(self.height) + \
               " width:" + str(self.width) + \
               " confidence:" + str(self.confidence)
