import time
from remotelib import Remote
from utils.Wheels import Wheels
from utils.IR import IR
from utils.Sounds import Sounds
from utils.Emotions import Emotions
from utils.LED import LED
from utils.Color import Color

from Robobo import Robobo

rob = Robobo("192.168.1.27")
rob.connect()

# Todos los comandos de movimiento pueden llevar un argumento más, que activa o desactiva la espera
# por ejemplo:
# rob.moveWheelsByDegree(Wheels.BOTH,90,50, False)


rob.moveWheelsByDegree(Wheels.BOTH,90,50)
rob.moveWheels(-10,-10,1)
rob.movePan(100,10)
rob.moveTilt(70,10)

rob.playNote(64,0.2)
rob.playNote(66,0.2)
rob.playNote(68,0.2)

rob.playEmotionSound(Sounds.APPROVE)

time.sleep(2)
rob.setLedColor(LED.All, Color.GREEN)

rob.talk("Hello world")

rob.setEmotion(Emotions.ANGRY)

time.sleep(2)
rob.setLedColor(LED.All, Color.RED)

rob.setEmotion(Emotions.LAUGTHING)

time.sleep(2)
rob.setLedColor(LED.All, Color.BLUE)

rob.setEmotion(Emotions.NORMAL)

time.sleep(2)

for element in IR:
    print("IR "+element.name+" value: "+ str(rob.getIR(element)))

print(rob.getBlob("green").posx)