class Blob:
    """
    Represents a blob detected:
        * color: (string) The color of the blob
        * posx: (int) The x coordinate of the center of the blob area
        * posy: (int) The y coordinate of the center of the blob area
        * size: (int) The area of the blob measured in pixels.
        * frame_timestamp: (long) The time when the frame started processing
        * status_timestamp: (long) The time when the status was sent
    """
    def __init__(self, color, posx, posy, size, frame_timestamp, status_timestamp):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.size = size
        self.frame_timestamp = frame_timestamp
        self.status_timestamp = status_timestamp


    def __str__(self):
        return self.color+" blob,  x:"+str(self.posx)+" y:"+str(self.posy)+" size:"+str(self.size) + " frame timestamp:"+str(self.frame_timestamp)