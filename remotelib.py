import json
import asyncio
import websockets

from threading import Thread

from state import State
from processors.PTProcessor import PTProcessor
from processors.RobProcessor import RobProcessor
from processors.VisionProcessor import VisionProcessor

class Remote:
    def __init__(self, ip):
        self.ip = ip
        self.ws = None
        self.password = ""
        self.disconnect = False;
        self.state = State()
        self.processors ={ "PT": PTProcessor(self.state),
                           "ROB": RobProcessor(self.state),
                           "Vision": VisionProcessor(self.state)}



    def wsStartup(self):
        self.ws = websockets.connect('ws://'+self.ip+':40404')
        print("Connecting")

        while not self.ws.connected:
            pass
        print("Connected")
    async def asyncStartup(self):
        async with websockets.connect('ws://'+self.ip+':40404') as ws:
            self.ws = ws
            await ws.send(f"PASSWORD: {self.password}")

            print(f"PASSWORD: {self.password}")
            while not self.disconnect:
                msg = await ws.recv()
                self.processMessage(msg)

    def startws(self):
        thread = Thread(target=self.asyncioThread())
        thread.start()

    def asyncioThread(self):
        asyncio.run_coroutine_threadsafe(self.asyncStartup())
        #asyncio.get_event_loop().run_until_complete(self.asyncStartup())
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


    def moveWheels(self, rspeed, lspeed, time):
        msg = self.processors["ROB"].moveWheelsSeparated(lspeed, rspeed, time)
        self.ws.send(msg)






