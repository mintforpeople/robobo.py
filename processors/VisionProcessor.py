import json

from processors.AbstractProcessor import AbstractProcessor
from utils.DetectedObject import DetectedObject
from utils.Lanes import LaneBasic, LanePro
from utils.Lines import Lines
from utils.Message import Message
from utils.QRCode import QRCode
from utils.Face import Face
from utils.Blob import Blob
from utils.Tag import Tag


class VisionProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["QRCODE", "FACE", "BLOB", "QRCODEAPPEAR", "QRCODELOST", "TAG", "DETECTED_OBJECT",
                                  "LANE_BASIC", "LANE_PRO", "LINE"]

        self.callbacklocks = {"qr": False,
                              "newqr": False,
                              "lostqr": False,
                              "face": False,
                              "lostface": False,
                              "blob": False,
                              "detectedobject": False,
                              "tag": False,
                              "lanepro": False,
                              "lanebasic": False,
                              "line": False}

        self.callbacks = {"qr": None,
                          "lostqr": None,
                          "newqr": None,
                          "face": None,
                          "lostface": None,
                          "blob": None,
                          "tag": None,
                          "detectedobject": None,
                          "lanepro": None,
                          "lanebasic": None,
                          "line": None}

    def process(self, status):
        name = status["name"]
        value = status["value"]

        if (name == "FACE"):
            if int(value["distance"]) >= 0:
                self.state.face = Face(int(value["coordx"]), int(value["coordy"]), int(value["distance"]))
                self.runCallback("face")

            else:
                self.runCallback("lostface")
                self.resetFace()

        elif (name == "BLOB"):
            self.state.blobs[value["color"]].posx = int(value["posx"])

            self.state.blobs[value["color"]].posy = int(value["posy"])

            self.state.blobs[value["color"]].size = int(value["size"])

            self.state.blobs[value["color"]].status_timestamp = int(value["timestamp"])

            self.state.blobs[value["color"]].frame_timestamp = int(value["frame_timestamp"])

            self.runCallback("blob")

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

            self.runCallback("newqr")


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
            self.runCallback("qr")



        elif (name == "QRCODELOST"):
            self.state.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None")
            self.runCallback("lostqr")

        elif name == "TAG":
            self.state.tag = Tag(int(value["cor1x"]),
                                 int(value["cor1y"]),
                                 int(value["cor2x"]),
                                 int(value["cor2y"]),
                                 int(value["cor3x"]),
                                 int(value["cor3y"]),
                                 int(value["cor4x"]),
                                 int(value["cor4y"]),
                                 float(value["rvec_0"]),
                                 float(value["rvec_1"]),
                                 float(value["rvec_2"]),
                                 float(value["tvec_0"]),
                                 float(value["tvec_1"]),
                                 float(value["tvec_2"]),
                                 value["id"])
            self.runCallback("tag")

        elif name == "DETECTED_OBJECT":
            self.state.detectedObject = DetectedObject(
                int(value["posx"]),
                int(value["posy"]),
                int(value["width"]),
                int(value["height"]),
                float(value["confidence"]),
                value["label"])
            self.runCallback("detectedobject")
        elif name == "LANE_BASIC":
            self.state.laneBasic = LaneBasic(
                float(value["a1"]),
                float(value["b1"]),
                float(value["a2"]),
                float(value["b2"]),
                int(value["id"]))
            self.runCallback("lanebasic")
        elif name == "LANE_PRO":
            self.state.lanePro = LanePro(
                float(value["left_a"]),
                float(value["left_b"]),
                float(value["left_c"]),
                float(value["right_a"]),
                float(value["right_b"]),
                float(value["right_c"]),
                json.loads(value["minv"]),
                int(value["id"]))
            self.runCallback("lanepro")
        elif name == "LINE":
            self.state.lines = Lines(
                json.loads(value["mat"]),
                int(value["id"]))
            self.runCallback("line")

    def configureBlobTracking(self, red, green, blue, custom):
        name = "CONFIGURE-BLOBTRACKING"
        id = self.state.getId()
        values = {"red": red,
                  "green": green,
                  "blue": blue,
                  "custom": custom}

        return Message(name, values, id)

    def resetBlobs(self):
        self.state.blobs = {
            "red": Blob("red", 0, 0, 0),
            "green": Blob("green", 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0)}

    def resetFace(self):
        self.state.face = Face(0, 0, -1)

    # Stream related functions
    # TODO: move all start/stop messages to a single file
    def startStream(self):
        name = "START-STREAM"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopStream(self):
        name = "STOP-STREAM"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startCamera(self):
        name = "START-CAMERA"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def setStreamFps(self, fps):
        name = "SET-STREAM-FPS"
        id = self.state.getId()
        values = {"fps": fps}
        return Message(name, values, id)

    def setCamera(self, camera):
        name = "SET-CAMERA"
        id = self.state.getId()
        values = {"camera": camera}
        return Message(name, values, id)

    def setCameraFps(self, fps):
        name = "SET-CAMERA-FPS"
        id = self.state.getId()
        values = {"fps": fps}
        return Message(name, values, id)

    def sendSync(self,syncId):
        name = "SYNC"
        id = self.state.getId()
        values = {"id":syncId}
        return Message(name, values, id)

    def stopCamera(self):
        name = "STOP-CAMERA"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startColorDetection(self):
        name = "START-COLOR-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopColorDetection(self):
        name = "STOP-COLOR-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startColorMeasurement(self):
        name = "START-COLOR-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopColorMeasurement(self):
        name = "STOP-COLOR-MEASUREMENT"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startFaceDetection(self):
        name = "START-FACE-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopFaceDetection(self):
        name = "STOP-FACE-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startObjectRecognition(self):
        name = "START-OBJECT-RECOGNITION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopObjectRecognition(self):
        name = "STOP-OBJECT-RECOGNITION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startQrTracking(self):
        name = "START-QR-TRACKING"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopQrTracking(self):
        name = "STOP-QR-TRACKING"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startTag(self):
        name = "START-TAG"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopTag(self):
        name = "STOP-TAG"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def changeTagSize(self, size):
        name = "CHANGE-SIZE-TAG"
        id = self.state.getId()
        values = {
            "size": size
        }
        return Message(name, values, id)

    def startLane(self):
        name = "START-LANE"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopLane(self):
        name = "STOP-LANE"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startLine(self):
        name = "START-LINE"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopLine(self):
        name = "STOP-LINE"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def startLineStats(self):
        name = "START-LINE-STATS"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopLineStats(self):
        name = "STOP-LINE-STATS"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def setLaneColorInversionOn(self):
        name = "INVERT-COLORS-LANE-ON"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def setLaneColorInversionOff(self):
        name = "INVERT-COLORS-LANE-OFF"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)
