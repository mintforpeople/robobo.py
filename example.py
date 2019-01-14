import time
from remotelib import Remote
from utils.Wheels import Wheels
from utils.IR import IR
from Robobo import Robobo

rob = Robobo("192.168.1.27")
rob.connect()

rob.moveWheelsByDegree(Wheels.BOTH,90,50)
rob.moveWheels(-10,-10,1)
rob.movePan(100,10)
rob.moveTilt(70,10)

while True:
    print(rob.getIR(IR.FrontC))
