import json
import websocket
import threading
import time
import sys

from robobopy.State import State
from robobopy.processors.PTProcessor import PTProcessor
from robobopy.processors.RobProcessor import RobProcessor
from robobopy.processors.VisionProcessor import VisionProcessor
from robobopy.processors.SmartphoneProcessor import SmartphoneProcessor
from robobopy.processors.SoundProcessor import SoundProcessor
from robobopy.utils.ConnectionState import ConnectionState


class Remote:
    def __init__(self, ip):
        self.ip = ip
        self.ws = None
        self.password = ""
        self.state = State()
        self.processors = {"PT": PTProcessor(self.state),
                           "ROB": RobProcessor(self.state),
                           "PHONE": SmartphoneProcessor(self.state),
                           "SOUND": SoundProcessor(self.state),
                           "VISION": VisionProcessor(self.state)}

        self.wsDaemon = None
        self.connectionState = ConnectionState.DISCONNECTED

        self.wheelsLastTime = 0
        self.panLastTime = 0
        self.tiltLastTime = 0

        self.timeout = 10

    def filterMovement(self, speed, axis):
        if speed == 0:
            return True
        elif axis == "wheels":
            millis = int(round(time.time() * 1000))
            return ((millis - self.wheelsLastTime) > self.timeout)

        elif axis == "pan":
            millis = int(round(time.time() * 1000))
            return ((millis - self.panLastTime) > self.timeout)

        elif axis == "tilt":
            millis = int(round(time.time() * 1000))
            return ((millis - self.tiltLastTime) > self.timeout)

    def disconnect(self):
        self.ws.close()
        self.connectionState = ConnectionState.DISCONNECTED

    def wsStartup(self):
        def on_open(ws):
            print("### connection established ###")
            ws.send("PASSWORD: " + self.password)
            self.connectionState = ConnectionState.CONNECTED

        def on_message(ws, message):
            self.processMessage(message)

        def on_error(ws, error):
            print(f"ERROR: {error}")
            self.connectionState = ConnectionState.ERROR

        def on_close(ws, status_code, msg):
            self.connectionState = ConnectionState.DISCONNECTED
            if (status_code != None):
                print(f"### closed connection [{status_code}] {msg} ###")
            else:
                print("### closed connection ###")

        self.ws = websocket.WebSocketApp('ws://' + self.ip + ":40404",
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)

        self.ws.on_open = on_open

        def runWS():
            self.ws.run_forever()

        self.wsDaemon = threading.Thread(target=runWS, name='wsDaemon')
        self.wsDaemon.setDaemon(True)
        self.wsDaemon.start()

        print("Connecting")
        self.connectionState = ConnectionState.CONNECTING

        while self.connectionState == ConnectionState.CONNECTING:
            print("wait")
            time.sleep(0.1)

    def processMessage(self, msg):
        status = json.loads(msg)
        name = status["name"]
        #print(name)
        #print(status)
        value = status["value"]
        processed = False
        for key in self.processors.keys():
            if self.processors[key].canProcess(name):
                self.processors[key].process(status)
                processed = True
                break

    def sendMessage(self, msg):
        if self.connectionState == ConnectionState.CONNECTED:
            try:
                self.ws.send(msg.encode())
            except websocket._exceptions.WebSocketConnectionClosedException:
                self.disconnect()
                sys.exit("\nError: Remote robot has forcefully disconnected. Re-establish the connection before sending a message")
        else:
            sys.exit("\nError: Establish connection before sending a message")

    def moveWheels(self, rspeed, lspeed, duration):
        if self.filterMovement(abs(rspeed) + abs(lspeed), "wheels"):
            msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, duration)
            self.sendMessage(msg)

    def moveWheelsWait(self, rspeed, lspeed, duration):
        if self.filterMovement(abs(rspeed) + abs(lspeed), "wheels"):
            msg = self.processors["ROB"].moveWheelsSeparatedWait(lspeed, rspeed, duration)
            self.sendMessage(msg)
            self.state.wheelLock = True
            while self.state.wheelLock:
                time.sleep(0.1)

    def moveWheelsByDegree(self, wheel, degrees, speed):
        if self.filterMovement(speed, "wheels"):
            msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
            self.sendMessage(msg)
        else:
            print('Robobo Warning: Ignored moveWheelsByDegree command. Maybe the client is sending messages too fast?')

    def moveWheelsByDegreeWait(self, wheel, degrees, speed):
        if self.filterMovement(speed, "wheels"):
            msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
            self.sendMessage(msg)
            self.state.wheelLock = True
            while self.state.wheelLock:
                time.sleep(0.1)
        else:
            print('Robobo Warning: Ignored moveWheelsByDegree command. Maybe the client is sending messages too fast?')

    def setLedColor(self, led, color):
        msg = self.processors["ROB"].setLedColor(led, color)
        self.sendMessage(msg)

    def resetEncoders(self):
        msg = self.processors["ROB"].resetEncoders()
        self.sendMessage(msg)

    def changeStatusFrequency(self, frequency):
        msg = self.processors["ROB"].changeStatusFrequency(frequency)
        self.sendMessage(msg)

    def movePan(self, pos, speed):
        if self.filterMovement(speed, "pan"):
            msg = self.processors["PT"].movePan(pos, speed)
            print(msg.encode())
            self.sendMessage(msg)
        else:
            print('Robobo Warning: Ignored movePan command. Maybe the client is sending messages too fast?')

    def movePanWait(self, pos, speed):
        if self.filterMovement(speed, "pan"):
            msg = self.processors["PT"].movePanWait(pos, speed)
            self.sendMessage(msg)
            self.state.panLock = True

            while self.state.panLock:
                time.sleep(0.1)
        else:
            print('Robobo Warning: Ignored movePan command. Maybe the client is sending messages too fast?')

    def moveTilt(self, pos, speed):
        if self.filterMovement(speed, "tilt"):
            msg = self.processors["PT"].moveTilt(pos, speed)
            self.sendMessage(msg)

        else:
            print('Robobo Warning: Ignored moveTilt command. Maybe the client is sending messages too fast?')

    def moveTiltWait(self, pos, speed):
        if self.filterMovement(speed, "tilt"):
            msg = self.processors["PT"].moveTiltWait(pos, speed)
            self.sendMessage(msg)
            self.state.tiltLock = True
            while self.state.tiltLock:
                time.sleep(0.1)
        else:
            print('Robobo Warning: Ignored moveTilt command. Maybe the client is sending messages too fast?')

    def playNote(self, index, duration, wait):
        msg = self.processors["SOUND"].playNote(index, int(duration * 1000))
        print(msg.encode())
        self.sendMessage(msg)
        if wait:
            time.sleep(duration)

    def playEmotionSound(self, sound):
        msg = self.processors["SOUND"].playEmotionSound(sound)
        print(msg.encode())
        self.sendMessage(msg)

    def talk(self, speech, wait):
        msg = self.processors["SOUND"].talk(speech)
        self.sendMessage(msg)
        if wait:
            self.state.talkLock = True
            while self.state.talkLock:
                time.sleep(0.1)

    def startStream(self):
        msg = self.processors["VISION"].startStream()
        self.sendMessage(msg)

    def stopStream(self):
        msg = self.processors["VISION"].stopStream()
        self.sendMessage(msg)

    def sendSync(self, syncId):
        msg = self.processors["VISION"].sendSync(syncId)
        self.sendMessage(msg)

    def startCamera(self):
        msg = self.processors["VISION"].startCamera()
        self.sendMessage(msg)

    def setStreamFps(self, fps):
        msg = self.processors["VISION"].setStreamFps(fps)
        self.sendMessage(msg)

    def setCameraFps(self, fps):
        msg = self.processors["VISION"].setCameraFps(fps)
        self.sendMessage(msg)

    def setCamera(self, camera):
        msg = self.processors["VISION"].setCamera(camera)
        self.sendMessage(msg)

    def stopCamera(self):
        msg = self.processors["VISION"].stopCamera()
        self.sendMessage(msg)

    def startColorDetection(self):
        msg = self.processors["VISION"].startColorDetection()
        self.sendMessage(msg)

    def stopColorDetection(self):
        msg = self.processors["VISION"].stopColorDetection()
        self.sendMessage(msg)

    def startColorMeasurement(self):
        msg = self.processors["VISION"].startColorMeasurement()
        self.sendMessage(msg)

    def stopColorMeasurement(self):
        msg = self.processors["VISION"].stopColorMeasurement()
        self.sendMessage(msg)

    def startFaceDetection(self):
        msg = self.processors["VISION"].startFaceDetection()
        self.sendMessage(msg)

    def stopFaceDetection(self):
        msg = self.processors["VISION"].stopFaceDetection()
        self.sendMessage(msg)

    def startObjectRecognition(self):
        msg = self.processors["VISION"].startObjectRecognition()
        self.sendMessage(msg)

    def stopObjectRecognition(self):
        msg = self.processors["VISION"].stopObjectRecognition()
        self.sendMessage(msg)

    def startQrTracking(self):
        msg = self.processors["VISION"].startQrTracking()
        self.sendMessage(msg)

    def stopQrTracking(self):
        msg = self.processors["VISION"].stopQrTracking()
        self.sendMessage(msg)

    def startTag(self):
        msg = self.processors["VISION"].startTag()
        self.sendMessage(msg)

    def stopTag(self):
        msg = self.processors["VISION"].stopTag()
        self.sendMessage(msg)

    def changeTagSize(self, size):
        msg = self.processors["VISION"].changeTagSize(size)
        self.sendMessage(msg)

    def startLane(self):
        msg = self.processors["VISION"].startLane()
        self.sendMessage(msg)

    def stopLane(self):
        msg = self.processors["VISION"].stopLane()
        self.sendMessage(msg)

    def startLine(self):
        msg = self.processors["VISION"].startLine()
        self.sendMessage(msg)

    def stopLine(self):
        msg = self.processors["VISION"].stopLine()
        self.sendMessage(msg)

    def startLineStats(self):
        msg = self.processors["VISION"].startLineStats()
        self.sendMessage(msg)

    def stopLineStats(self):
        msg = self.processors["VISION"].stopLineStats()
        self.sendMessage(msg)

    def setLaneColorInversionOn(self):
        msg = self.processors["VISION"].setLaneColorInversionOn()
        self.sendMessage(msg)

    def setLaneColorInversionOff(self):
        msg = self.processors["VISION"].setLaneColorInversionOff()
        self.sendMessage(msg)

    def resetClaps(self):
        self.processors["SOUND"].resetClaps()

    def resetTap(self):
        self.processors["PHONE"].resetTap()

    def resetFling(self):
        self.processors["PHONE"].resetFling()

    def resetBlobs(self):
        self.processors["VISION"].resetBlobs()

    def resetFace(self):
        self.processors["VISION"].resetFace()

    def setEmotionTo(self, emotion):
        msg = self.processors["PHONE"].setEmotion(emotion)
        self.sendMessage(msg)

    def configureBlobTracking(self, red, green, blue, custom):
        msg = self.processors["VISION"].configureBlobTracking(red, green, blue, custom)
        self.sendMessage(msg)

    def advancedLostBlobConfiguration(self,  frames, minarea, max_count, epsilon):
        msg = self.processors["VISION"].advancedLostBlobConfiguration(frames, minarea, max_count, epsilon)
        self.sendMessage(msg)

    def setClapCallback(self, callback):
        self.processors["SOUND"].callbacks["clap"] = callback

    def setNoteCallback(self, callback):
        self.processors["SOUND"].callbacks["note"] = callback

    def setTalkCallback(self, callback):
        self.processors["SOUND"].callbacks["talk"] = callback

    def setFaceCallback(self, callback):
        self.processors["VISION"].callbacks["face"] = callback

    def setLostFaceCallback(self, callback):
        self.processors["VISION"].callbacks["lostface"] = callback

    def setBlobCallback(self, callback):
        self.processors["VISION"].callbacks["blob"] = callback

    def setQRCallback(self, callback):
        self.processors["VISION"].callbacks["qr"] = callback

    def setNewQRCallback(self, callback):
        self.processors["VISION"].callbacks["newqr"] = callback

    def setLostQRCallback(self, callback):
        self.processors["VISION"].callbacks["lostqr"] = callback

    def setTapCallback(self, callback):
        self.processors["PHONE"].callbacks["tap"] = callback

    def setFlingCallback(self, callback):
        self.processors["PHONE"].callbacks["fling"] = callback

    def setTagCallback(self, callback):
        self.processors["VISION"].callbacks["tag"] = callback

    def setDetectedObjectCallback(self, callback):
        self.processors["VISION"].callbacks["detectedobject"] = callback

    def setLineCallback(self, callback):
        self.processors["VISION"].callbacks["line"] = callback

    def setLaneBasicCallback(self, callback):
        self.processors["VISION"].callbacks["lanebasic"] = callback

    def setLaneProCallback(self, callback):
        self.processors["VISION"].callbacks["lanepro"] = callback
