class DetectedObject:
    """
    Represents an object detected by Robobo.

    Attributes:
        - x (int): The x coordinate of the center of the bounding box, measured in pixels from the left side of the screen. Takes positive values.
        - y (int): The y coordinate of the center of the bounding box, measured in pixels from the upper side of the screen. Takes positive values.
        - width (int): The width of the bounding box, measured in pixels. Takes positive values.
        - height (int): The height of the bounding box, measured in pixels. Takes positive values.
        - label (string): The class of the identified object.
        - confidence (float): The confidence for the class of the object. Takes values between 0.5 and 1.
    """

    def __init__(self, x, y, width, height, confidence, label, statusTimestamp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.confidence = confidence
        self.timeStamp = statusTimestamp

    def __str__(self):
        return "DETECTED_OBJECT, Label:" + self.label + \
               " x:" + str(self.x) + \
               " y:" + str(self.y) + \
               " height:" + str(self.height) + \
               " width:" + str(self.width) + \
               " confidence:" + str(self.confidence) + \
               " timestamp:" + str(self.timeStamp)
