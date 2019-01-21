import json
import websocket
import threading
import time

from State import State
from processors.PTProcessor import PTProcessor
from processors.RobProcessor import RobProcessor
from processors.VisionProcessor import VisionProcessor
from processors.SmartphoneProcessor import SmartphoneProcessor
from processors.SoundProcessor import SoundProcessor
from utils.ConnectionState import ConnectionState
from utils.IR import IR
class Remote:
    def __init__(self, ip):
        self.ip = ip
        self.ws = None
        self.password = ""
        self.disconnect = False
        self.state = State()
        self.processors ={ "PT": PTProcessor(self.state),
                           "ROB": RobProcessor(self.state),
                           "PHONE": SmartphoneProcessor(self.state),
                           "SOUND": SoundProcessor(self.state),
                           "VISION": VisionProcessor(self.state)}

        self.wsDaemon = None
        self.connectionState = ConnectionState.DISCONNECTED





    def wsStartup(self):
        def on_open(ws):
            print("Open")
            ws.send("PASSWORD: "+self.password)
            self.connectionState = ConnectionState.CONNECTED

        def on_message(ws, message):
            self.processMessage(message)

        def on_error(ws, error):
            print(error)
            self.connectionState = ConnectionState.ERROR

        def on_close(ws):
            self.connectionState = ConnectionState.DISCONNECTED
            print("### closed connection ###")

        self.ws = websocket.WebSocketApp('ws://'+self.ip+":40404",
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


    def processMessage(self,msg):
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
            self.ws.send(msg.encode())
        else:
            print("Error: Stablish connection before sending a message")

    def moveWheels(self, rspeed, lspeed, duration):
        msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, duration)
        self.sendMessage(msg)

    def moveWheelsWait(self, rspeed, lspeed, duration):
        msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, duration)
        self.sendMessage(msg)

        time.sleep(duration-0.15)

    def moveWheelsByDegree(self, wheel, degrees, speed ):
        msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
        self.sendMessage(msg)

    def moveWheelsByDegreeWait(self, wheel, degrees, speed ):
        msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
        self.sendMessage(msg)
        self.state.wheelLock = True
        while self.state.degreesLock:
            time.sleep(0.1)

    def setLedColor(self,led, color):
        msg = self.processors["ROB"].setLedColor(led,color)
        self.sendMessage(msg)

    def resetEncoders(self):
        msg = self.processors["ROB"].resetEncoders()
        self.sendMessage(msg)


    def movePan(self, pos, speed):
        msg = self.processors["PT"].movePan(pos, speed)
        print(msg.encode())
        self.sendMessage(msg)

    def movePanWait(self, pos, speed):
        msg = self.processors["PT"].movePanWait(pos, speed)
        self.sendMessage(msg)
        self.state.panLock = True

        while self.state.panLock:
            time.sleep(0.1)

    def moveTilt(self, pos, speed):
        msg = self.processors["PT"].moveTilt(pos, speed)
        self.sendMessage(msg)

    def moveTiltWait(self, pos, speed):
        msg = self.processors["PT"].moveTiltWait(pos, speed)
        self.sendMessage(msg)
        self.state.tiltLock = True
        while self.state.tiltLock:
            time.sleep(0.1)

    def playNote(self, index, duration, wait):
        msg = self.processors["SOUND"].playNote(index, int(duration*1000))
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

    def resetClaps(self):
        self.processors["SOUND"].resetClaps()


    def setEmotion(self, emotion):
        msg = self.processors["PHONE"].setEmotion(emotion)
        self.sendMessage(msg)


    def configureBlobTracking(self, red, green, blue, custom):
        msg = self.processors["VISION"].configureBlobTracking(red, green, blue, custom)
        self.sendMessage(msg)


