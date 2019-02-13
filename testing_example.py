
from utils.Wheels import Wheels
from utils.IR import IR
from utils.Sounds import Sounds
from utils.Emotions import Emotions
from utils.LED import LED
from utils.Color import Color

from Robobo import Robobo


def testMoveWheels():
    rob.moveWheelsByTime(10,10,2,wait=False)
    rob.movePanTo(60,20)
    rob.wait(1)
    rob.moveWheelsByTime(10, 10, 1)
    rob.movePanTo(90,20)
    rob.wait(1)
    rob.moveWheelsByDegree(Wheels.BOTH,90,10)
    rob.movePanTo(0, 20)
    rob.wait(1)
    posL = rob.readWheelPosition(Wheels.L)
    print ("PosL: " + str(posL))
    posR = rob.readWheelPosition(Wheels.R)
    print ("PosR: " + str(posR))


def testLeds():
    rob.sayText("Testing my leds")
    rob.setLedColorTo(LED.All, Color.RED)
    rob.wait(0.5)
    rob.setLedColorTo(LED.All, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontC, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontC, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontLL, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontLL, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontL, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontL, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontR, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontR, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontRE, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.FrontRE, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.BackL, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.BackL, Color.OFF)
    rob.wait(0.5)
    rob.setLedColorTo(LED.BackR, Color.MAGENTA)
    rob.wait(0.5)
    rob.setLedColorTo(LED.BackR, Color.OFF)
    rob.wait(0.5)
    rob.sayText("Finished!")


def testIRAndLeds():
    closeIRValue = 100
    mediumIRValue = 20
    farIRValue = 5
    speed = 1

    rob.setLedColorTo(LED.All,Color.OFF)
    rob.moveWheels(speed,speed)

    print(rob.readAllIRSensor())
    while (rob.readIRSensor(IR.FrontC) < farIRValue)and(rob.readIRSensor(IR.FrontRR) < farIRValue)and(rob.readIRSensor(IR.FrontLL) < farIRValue):
        rob.wait(0.1)
        print(rob.readAllIRSensor())

    rob.setLedColorTo(LED.All,Color.GREEN)

    while (rob.readIRSensor(IR.FrontC) < mediumIRValue)and(rob.readIRSensor(IR.FrontRR) < mediumIRValue)and(rob.readIRSensor(IR.FrontLL) < mediumIRValue):
        rob.wait(0.1)
        print(rob.readAllIRSensor())

    rob.setLedColorTo(LED.All,Color.MAGENTA)

    while (rob.readIRSensor(IR.FrontC) < closeIRValue)and(rob.readIRSensor(IR.FrontRR) < closeIRValue)and(rob.readIRSensor(IR.FrontLL) < closeIRValue):
        rob.wait(0.1)

    rob.stopMotors()
    rob.setLedColorTo(LED.All,Color.RED)
    rob.setEmotionTo(Emotions.SURPRISED)
    rob.playSound(Sounds.DISCOMFORT)
    #rob.moveWheelsByTime(speed*-1,speed*-1,1)
    rob.setLedColorTo(LED.All,Color.BLUE)
    rob.setEmotionTo(Emotions.SURPRISED)



def flingDetectedCallback():
    rob.sayText("Fling detected!")


def tapDetectedCallback():
    rob.stopMotors()
    print("--> TAP detected -> x: "+str(rob.readTapSensor("x")) + ", y:"+str(rob.readTapSensor("y")))


def faceDetectedCallback():
    face = rob.readFaceSensor()
    print("--> New face detected. Distance: " + str(face.distance) + ", (x,y): " + str(face.posx) + ", "+str(face.posy))

def faceLostCallback():
    print("--> Face Lost !!")

def newColorBlobDetectedCallback():
    rob.sayText("Blob detected")


def anewQRCodeDetectedCallback():
    qr = rob.readQR()
    rob.sayText("New QR detected")
    print("--> New QR detected: " + str(qr))

def aQRCodeDetectedCallBack():
    qr = rob.readQR()
    rob.sayText("QR detected")
    print("--> QR detected: " + str(qr))

def clapDetectedCallBack():
    print("--> CLAP DETECTED!!")


if __name__ == '__main__':
    rob = Robobo("10.113.36.195")
    rob.connect()
    # rob.setEmotionTo(Emotions.NORMAL)
    # rob.setActiveBlobs(True, True, False, False)
    # rob.moveTiltTo(75,20,wait=False)
    # rob.movePanTo(0,20)
    # rob.wait(1)
    #
    # rob.whenAFlingIsDetected(flingDetectedCallback)
    # rob.whenATapIsDetected(tapDetectedCallback)
    # rob.whenANewFaceIsDetected(faceDetectedCallback)
    # rob.whenAFaceIsLost(faceLostCallback())
    # #rob.whenANewColorBlobIsDetected(newColorBlobDetectedCallback)
    # rob.whenANewQRCodeIsDetected(anewQRCodeDetectedCallback)
    # #rob.whenAQRCodeIsDetected(aQRCodeDetectedCallBack)
    # rob.whenClapIsDetected(clapDetectedCallBack())

    #testLeds()
    #testIRAndLeds()
    #testMoveWheels()

    # rob.playNote(52,1)
    # rob.playNote(55, 1)
    # rob.playNote(60, 1)
    # print("Last Note --> " + rob.readLastNote())

    while (True):
        print()
        print("IR Sensor values: " + str(rob.readAllIRSensor()))
        print("IR Blob values: ")
        blobs = rob.readAllColorBlobs()
        for key in blobs:
            print("- "+str(blobs[key].color)+": (x,y)"+str(blobs[key].posx)+", "+str(blobs[key].posy)+" - size: " + str(blobs[key].size))
        print("Brightness: " + str(rob.readBrightnessSensor()))
        print("Phone battery level: " + str(rob.readBatteryLevel("phone")))
        print("Base battery level: "+ str(rob.readBatteryLevel("base")))

        #print("Orientation sensor:" + str(rob.readOrientationSensor()))

        print("Acceleration sensor: " + str(rob.readAccelerationSensor("x"))
              + ", " + str(rob.readAccelerationSensor("y"))
              + ", " + str(rob.readAccelerationSensor("x")))

        print()

        rob.wait(1)




