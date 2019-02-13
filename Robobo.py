from remotelib import Remote
from utils.Wheels import Wheels
from utils.Note import Note
import time

class Robobo:
    """
     Robobo.py is the library used to create programs for the Robobo educational
     robot (http://www.theroboboproject.com) in the Python language.

     For more information and documentation see <URL WIKI>

    """
    def __init__(self, ip):
        """
        Creates a new Robobo.js library instance.

        :param ip: (string) The IP address of the Robobo robot
        """
        self.rem = Remote(ip)

    def connect(self):
        """
        Establishes a remote connection with the Robobo indicated by the IP address associated to this instance.
        """
        self.rem.wsStartup()

    def disconnect(self):
        """
        Disconnects the library from the Robobo robot.
        """
        self.rem.disconnect()

    def wait(self, seconds):
        """
        Pauses the program for the specified time (in seconds)
        :param seconds: (float) Time in seconds (accepts decimals like 0.2)
        """
        time.sleep(seconds)

    def moveWheelsByTime(self, rSpeed, lSpeed, duration, wait = True):
        """
        Moves the wheels of the robot at the specified speeds during the specified time.

        :param rSpeed: (int) Speed factor for the right wheel [-100..100]
        :param lSpeed: (int) Speed factor for the left wheel [-100..100]
        :param duration: (int) Time duration of the movement in seconds
        :param wait: (boolean) True - blocking mode, False - non blocking mode

        """
        if wait:
            self.rem.moveWheelsWait(rSpeed, lSpeed, duration)
        else:
            self.rem.moveWheels(rSpeed, lSpeed, duration)

    def moveWheels(self, rSpeed, lSpeed):
        """
        Starts moving the wheels of the robot at the specified speed.
        
        :param rSpeed: (int) Speed factor for the right wheel [-100 - 100]
        :param lSpeed: (int) Speed factor for the left wheel [-100 - 100]

        """
        self.rem.moveWheels(rSpeed, lSpeed, 100000)

    def stopMotors(self):
        self.rem.moveWheels(0,0,1)

    def moveWheelsByDegree(self, wheel, degrees, speed):
        """
        Moves the wheels of the robot by some degress at the specified speed.

        :param wheel: (enum) Wheels to move, one value of the Wheels enumeration  (see :class:`~utils.Wheels`)
        :param degrees: (int) Degress to move the wheel
        :param speed: (int) Speed factor for the right wheel [-100 - 100]

        """
        self.rem.moveWheelsByDegreeWait(wheel,degrees,speed)

    def movePanTo(self, degrees, speed, wait = True):
        """
        Moves the PAN of the base to the specified position at the specified speed

        :param degrees: (int) Position in degress of the PAN [-160..160]
        :param speed: (int) Speed factor [-40..40]
        :param wait:  (boolean) True: blocking mode, False: non-blocking mode
        """
        if wait:
            self.rem.movePanWait(degrees, speed)
        else:
            self.rem.movePan(degrees, speed)

    def moveTiltTo(self, degrees, speed, wait = True):
        """
        Moves the TILT of the base to the specified position at the specified speed

        :param degrees: (int) Position in degrees of the TILT [5..105]
        :param speed: (int) Speed factor [-10..10]
        :param wait: (boolean) True: blocking mode, False: non-blocking mode
        """
        if wait:
            self.rem.moveTiltWait(degrees, speed)
        else:
            self.rem.moveTilt(degrees, speed)

    def setLedColorTo(self, led, color):
        """
        Changes the color of a LED of the base

        :param led: (enum) One value of the LED enumeration (see :class:`~utils.LED`)
        :param color: (enum) One value of the  Color enumeration (see :class:~utils.Color`)

        """
        self.rem.setLedColor(led, color)

    def resetWheelEncoders(self):
        """
        Resets the encoders of the wheels
        """
        self.rem.resetEncoders()

    def playNote(self, note, duration, wait = True):
        """
        Commands the robot to play a musical note

        :param note: (integer) Musical note index [48..72]. Anglo-Saxon notation is used and there are 25 possible notes with the following basic correspondence. Any integer between 48 and 72.
        :param duration: (integer) Duration of the note in seconds (decimals can be used to used, like 0.2 or 0.5)
        :param wait: (boolean) True: blocking mode, False: non-blocking mode
        """
        self.rem.playNote(note, duration, wait)

    def playSound(self, sound):
        """
        Commands the robot to play the specified emotion sound

        :param sound: (enum) One value of the Sound enumeration (see :class:`~utils.Sounds`)
        """
        self.rem.playEmotionSound(sound)

    def sayText(self, speech, wait = True):
        """
        Commands the robot say the specified text

        :param speech: (string) The text to say
        :param wait: (boolean) True: blocking mode, False: non-blocking mode
        """
        self.rem.talk(speech, wait)

    def resetClapCounter(self):
        """
        Resets the clap counter

        """
        self.rem.resetClaps()

    def resetTapSensor(self):
        """
        Resets the tap sensor value
        """
        self.rem.resetTap()

    def resetFlingSensor(self):
        """
        Resets the state of the Fling sensor
        """
        self.rem.resetFling()

    def resetColorBlobs(self):
        """
        Resets the color blob detector
        """
        self.rem.resetBlobs()

    def resetFaceSensor(self):
        """
        Resets the face sensor. After this function, and until a new face is detected, the face sensor will return 0 as values for distance, x and y position.
        """
        self.rem.resetFace()

    def setEmotionTo(self, emotion):
        """
        Changes the emotion of showed by the face of Robobo
        :param emotion: One value of the Emotion enumeration (see :class:`~utils.Emotions`)
        """
        self.rem.setEmotionTo(emotion)

    def setActiveBlobs(self, red, green, blue, custom):
        """
        Activates the individual tracking of each color.

        *Warning*: Color tracking is a computionally intensive task, activating all the colors may impact performance

        :param red: (boolean) Enables red blob tracking
        :param green: (boolean) Enables green blob tracking
        :param blue: (boolean) Enables blue blob tracking
        :param custom: (boolean) Enables custom blob tracking
        """
        self.rem.configureBlobTracking(red, green, blue, custom)

    def readClapCounter(self):
        return self.rem.state.claps

    def readLastNote(self):
        return Note(self.rem.state.lastNote, self.rem.state.lastNoteDuration)

    def readIRSensor(self, id):
        if self.rem.state.irs == []:
            return 0
        else:
            return int(self.rem.state.irs[id.value])

    def readAllIRSensor(self):
        return self.rem.state.irs

    def readColorBlob(self, color):
        return self.rem.state.blobs[color]

    def readAllColorBlobs(self):
        return self.rem.state.blobs

    def readQR(self):
        return self.rem.state.qr

    def readOrientationSensor(self, axis):
        if axis == "yaw":
            return self.rem.state.yaw
        elif axis == "pitch":
            return self.rem.state.pitch
        elif axis == "roll":
            return self.rem.state.roll

    def readAccelerationSensor(self, axis):
        if axis == "x":
            return self.rem.state.accelx
        elif axis == "y":
            return self.rem.state.accely
        elif axis == "z":
            return self.rem.state.accelz

    def readTapSensor(self, axis):
        if axis == "x":
            return self.rem.state.tapx
        elif axis == "y":
            return self.rem.state.tapy

    def readPanPosition(self):
        return self.rem.state.panPos

    def readTiltPosition(self):
        return self.rem.state.tiltPos

    def readWheelPosition(self, wheel):
        if wheel == Wheels.R:
            return self.rem.state.wheelPosR
        elif wheel == Wheels.L:
            return self.rem.state.wheelPosL
        else:
            print("Wheel id not valid")
            return 0

    def readWheelSpeed(self, wheel):
        if wheel.value == Wheels.R:
            return self.rem.state.wheelSpeedR
        elif wheel.value == Wheels.L:
            return self.rem.state.wheelSpeedL
        else:
            print("Wheel id not valid")
            return 0

    def readFlingAngle(self):
        return self.rem.state.flingAngle

    def readFlingDistance(self):
        return self.rem.state.flingDistance

    def readFlingTime(self):
        return self.rem.state.flingTime

    def readBatteryLevel(self, device):
        if device == "phone":
            return self.rem.state.phoneBattery
        else:
            return self.rem.state.baseBattery

    def readNoiseLevel(self):
        return self.rem.state.noise

    def readBrightnessSensor(self):
        return self.rem.state.brightness

    def readFaceSensor(self):
        return self.rem.state.face

    def whenClapIsDetected(self, callback):
        self.rem.setClapCallback(callback)

    def whenANoteIsDetected(self, callback):
        self.rem.setNoteCallback(callback)

    def whenANewFaceIsDetected(self, callback):
        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        self.rem.setNewQRCallback(callback)

    def whenATapIsDetected(self, callback):
        self.rem.setTapCallback(callback)

    def whenAFlingIsDetected(self, callback):
        self.rem.setFlingCallback(callback)

    def whenAFaceIsLost(self, callback):
        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        self.rem.setLostQRCallback(callback)

    def changeStatusFrequency(self, frequency):
        self.rem.changeStatusFrequency(frequency)

