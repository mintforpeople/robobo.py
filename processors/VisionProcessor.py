
from processors.AbstractProcessor import AbstractProcessor
from utils.Message import Message
from utils.QRCode import QRCode
from utils.Face import Face
class VisionProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["QRCODE","FACE","BLOB","QRCODEAPPEAR","QRCODELOST"]
        self.qrCallback=   None
        self.faceCallback= None
        self.blobCallback= None

    def process(self, status):
        name = status["name"]
        value = status["value"]
        print(name)

        if (name == "FACE"):
            self.state.face = Face(int(value["coordx"]),int(value["coordy"]), int(value["distance"]))
            self.runCallback(self.faceCallback)

        elif (name == "BLOB"):
            print(status)
            self.state.blobs[value["color"]].posx = int(value["posx"])

            self.state.blobs[value["color"]].posy = int(value["posy"])

            self.state.blobs[value["color"]].size = int(value["size"])

            self.runCallback(self.blobCallback)

        elif (name == "QRCODEAPPEAR"):

            self.state.qr = QRCode(float(value["coordx"]),
                             float(value["coordy"]),
                             float(value["distance"]),
                             float(value["p1x"]),
                             float(value["p1y"]),
                             float(value["p2x"]),
                             float(value["p2y"]),
                             float(value["p3x"]),
                             float(value["p3y"]),
                             value["id"])

            self.runCallback(self.qrCallback)


        elif (name == "QRCODE"):
            self.state.qr = QRCode(float(value["coordx"]),
                             float(value["coordy"]),
                             float(value["distance"]),
                             float(value["p1x"]),
                             float(value["p1y"]),
                             float(value["p2x"]),
                             float(value["p2y"]),
                             float(value["p3x"]),
                             float(value["p3y"]),
                             value["id"])
            print(self.state.qr)


        elif (name == "QRCODELOST"):
            self.state.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None")



    def configureBlobTracking(self, red, green, blue, custom):
        name = "CONFIGURE-BLOBTRACKING"
        id = self.state.getId()
        values = {"red": red,
                  "green": green,
                  "blue": blue,
                  "custom": custom}

        return Message(name, values, id)


