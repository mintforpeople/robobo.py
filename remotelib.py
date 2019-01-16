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
        self.connected = False






    def wsStartup(self):
        def on_open(ws):
            print("Open")
            ws.send("PASSWORD: "+self.password)
            self.connected = True

        def on_message(ws, message):
            self.processMessage(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            self.connected = False
            print("### closed ###")

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
        while not self.connected:
            print("wait")
            time.sleep(0.1)


    def processMessage(self,msg):
        status = json.loads(msg)
        name = status["name"]
        value = status["value"]
        processed = False
        for key in self.processors.keys():
            if self.processors[key].canProcess(name):
                self.processors[key].process(status)
                processed = True
                break


    def moveWheels(self, rspeed, lspeed, duration):
        msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, duration)
        print(msg.encode())
        self.ws.send(msg.encode())

    def moveWheelsWait(self, rspeed, lspeed, duration):
        msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, duration)
        print(msg.encode())
        self.ws.send(msg.encode())

        time.sleep(duration-0.15)

    def moveWheelsByDegree(self, wheel, degrees, speed ):
        msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
        print(msg.encode())
        self.ws.send(msg.encode())

    def moveWheelsByDegreeWait(self, wheel, degrees, speed ):
        msg = self.processors["ROB"].moveWheelsByDegree(wheel, degrees, speed)
        print(msg.encode())
        self.ws.send(msg.encode())
        self.state.wheelLock = True
        while self.state.degreesLock:
            time.sleep(0.1)

    def resetEncoders(self):
        msg = self.processors["ROB"].resetEncoders()
        self.ws.send(msg.encode())


    def movePan(self, pos, speed):
        msg = self.processors["PT"].movePan(pos, speed)
        print(msg.encode())
        self.ws.send(msg.encode())

    def movePanWait(self, pos, speed):
        msg = self.processors["PT"].movePanWait(pos, speed)
        print(msg.encode())
        self.ws.send(msg.encode())
        self.state.panLock = True

        while self.state.panLock:
            time.sleep(0.1)

    def moveTilt(self, pos, speed):
        msg = self.processors["PT"].moveTilt(pos, speed)
        print(msg.encode())
        self.ws.send(msg.encode())

    def moveTiltWait(self, pos, speed):
        msg = self.processors["PT"].moveTiltWait(pos, speed)
        print(msg.encode())
        self.ws.send(msg.encode())
        self.state.tiltLock = True
        while self.state.tiltLock:
            time.sleep(0.1)

