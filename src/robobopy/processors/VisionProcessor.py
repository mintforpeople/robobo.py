import json

from robobopy.processors.AbstractProcessor import AbstractProcessor
from robobopy.utils.DetectedObject import DetectedObject
from robobopy.utils.Face import Face
from robobopy.utils.Lanes import LaneBasic, LanePro
from robobopy.utils.Lines import Lines
from robobopy.utils.Message import Message
from robobopy.utils.Blob import Blob
from robobopy.utils.QRCode import QRCode
from robobopy.utils.Tag import Tag


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
                              "newtag": False,
                              "losttag": False,
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
                          "newtag": None,
                          "losttag": None,
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
            if "timestamp" in value.keys():
                self.state.blobs[value["color"]].status_timestamp = int(value["timestamp"])
            if "frame_timestamp" in value.keys():
                self.state.blobs[value["color"]].frame_timestamp = int(value["frame_timestamp"])
            self.runCallback("blob")

        elif name == "QRCODEAPPEAR":
            self.state.qr = QRCode(float(value["coordx"]),
                                   float(value["coordy"]),
                                   float(value["distance"]),
                                   0,0,
                                   0,0,
                                   0,0,
                                   value["id"], 0)

            self.runCallback("newqr")

        elif name == "QRCODE":
            self.state.qr = QRCode(float(value["coordx"]),
                                   float(value["coordy"]),
                                   float(value["distance"]),
                                   float(value["p1x"]),
                                   float(value["p1y"]),
                                   float(value["p2x"]),
                                   float(value["p2y"]),
                                   float(value["p3x"]),
                                   float(value["p3y"]),
                                   value["id"], int(value["timestamp"]))
            self.runCallback("qr")




        elif (name == "QRCODELOST"):
            self.state.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None", 0)

            self.runCallback("lostqr")

        elif name == "TAG":
            taglist = json.loads(value["tags"])
            tags = []
            for tag in taglist:
                tagobject = Tag(int(tag["cor1x"]),
                                    int(tag["cor1y"]),
                                    int(tag["cor2x"]),
                                    int(tag["cor2y"]),
                                    int(tag["cor3x"]),
                                    int(tag["cor3y"]),
                                    int(tag["cor4x"]),
                                    int(tag["cor4y"]),
                                    float(tag["rvec_0"]),
                                    float(tag["rvec_1"]),
                                    float(tag["rvec_2"]),
                                    float(tag["tvec_0"]),
                                    float(tag["tvec_1"]),
                                    float(tag["tvec_2"]),
                                    tag["id"], int(value["timestamp"]))
                tags += [tagobject]
            self.state.tags = tags
            self.runCallback("tag")
        
        elif name == "TAGAPPEAR":
            self.state.newestTag = Tag(int(value["cor1x"]),
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
                                    value["id"], int(value["timestamp"]))
            self.runCallback("newtag")

        elif name == "TAGLOST":
            self.state.lastLostTagId = value["id"]
            self.runCallback("losttag")

        elif name == "DETECTED_OBJECT":
            self.state.detectedObject = DetectedObject(
                int(value["posx"]),
                int(value["posy"]),
                int(value["width"]),
                int(value["height"]),
                float(value["confidence"]),
                value["label"],int(value["timestamp"]))
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

    def advancedLostBlobConfiguration(self, frames, minarea, max_count, epsilon):
        name = "CONFIGURE-LOSTBLOB"
        id = self.state.getId()
        values = {"frames": frames,
                  "minarea": minarea,
                  "max_count": max_count,
                  "epsilon": epsilon}

        return Message(name, values, id)

    def resetBlobs(self):
        self.state.blobs = {

            "red": Blob("red", 0, 0, 0, 0, 0),
            "green": Blob("green", 0, 0, 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0, 0, 0)}


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
