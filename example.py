import time
from remotelib import Remote
from utils.Wheels import Wheels

rmlib = Remote("192.168.31.160")

rmlib.wsStartup()

rmlib.moveWheelsByDegreeWait(Wheels.R, 360, 20)



print("END")

time.sleep(30)
