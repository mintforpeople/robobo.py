import time
from remotelib import Remote
from utils.Wheels import Wheels
from utils.IR import IR
from utils.Sounds import Sounds
from utils.Emotions import Emotions
from utils.LED import LED
from utils.Color import Color

from Robobo import Robobo

rob = Robobo("192.168.1.58")
rob.connect()

rob.moveWheelsByDegrees(Wheels.BOTH,90,50)
rob.moveWheelsByTime(-10,-10,1)
rob.movePanTo(0, 10)
rob.moveTiltTo(70, 10)

rob.playNote(64,0.2)
rob.playNote(66,0.2)
rob.playNote(68,0.2)

rob.playSound(Sounds.APPROVE)

time.sleep(2)
rob.setLedColorTo(LED.All, Color.GREEN)

rob.sayText("Hello world")

rob.setEmotionTo(Emotions.ANGRY)

time.sleep(1)
rob.setLedColorTo(LED.All, Color.RED)

rob.setEmotionTo(Emotions.LAUGHING)

time.sleep(1)
rob.setLedColorTo(LED.All, Color.BLUE)

rob.setEmotionTo(Emotions.NORMAL)

rob.resetClapCounter()
print("Now Clap")
time.sleep(3)
print("You clapped " + str(rob.readClapCounter()) + " times")


for element in IR:
    print("IR " + element.name + " value: " + str(rob.readIRSensor(element)))
print(rob.readColorBlob("green"))

rob.disconnect()