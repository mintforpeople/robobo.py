class DetectedObject:
    """
    Represents a detected object

    Attributes:
        - x: x coordinate of the bounding box.
        - y: x coordinate of the bounding box.
        - width: width of the bounding box.
        - height: height of the bounding box.
        - label: class of the identified object.
        - confidence: confidence or score of the class of the object.
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
