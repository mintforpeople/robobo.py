from remotelib import Remote
from utils.Wheels import Wheels
from utils.Note import Note
from utils.Acceleration import Acceleration
from utils.Orientation import Orientation
from utils.Tap import Tap
import time

class Robobo:

    """
     Robobo.py is the library used to create programs for the Robobo educational
     robot (http://www.theroboboproject.com) in the Python language.

     For more information and documentation see <URL WIKI>

     To create a Robobo.py instance:

     .. code-block:: python

        from Robobo import Robobo

        rob = Robobo ('10.113.36.150')

     **Parameters:**

     - **ip:** (string) The IP address of the Robobo robot

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
        """
        Stops the movement of the wheels
        """
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
        :param color: (enum) One value of the  Color enumeration (see :class:`~utils.Color`)

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

        **Warning**: Color tracking is a computionally intensive task, activating all the colors may impact performance

        :param red: (boolean) Enables red blob tracking
        :param green: (boolean) Enables green blob tracking
        :param blue: (boolean) Enables blue blob tracking
        :param custom: (boolean) Enables custom blob tracking
        """
        self.rem.configureBlobTracking(red, green, blue, custom)

    def readClapCounter(self):
        """
        Returns the number of claps registered since the last reset

        :return: (integer) Clap counter
        """
        return self.rem.state.claps

    def readLastNote(self):
        """
        Returns the last note detected by the note sensor

        :return: (Note) A Note object (see :class:`~utils.Note`)
        """
        return Note(self.rem.state.lastNote, self.rem.state.lastNoteDuration)

    def readIRSensor(self, id):
        """
        Returns the current value sensed by the specified IR

        :param id: (enum) One value of the Ir enumeration (see :class:`~utils.IR`)
        :return:
        """
        if self.rem.state.irs == []:
            return 0
        else:
            return int(self.rem.state.irs[id.value])

    def readAllIRSensor(self):
        """
        Returns the values of all the IR sensors.

        Example of use:

        .. code-block:: python

            irs = rob.readAllIRSensor()
            if irs != []:
                print (irsensors[IR.FrontR.value])
                print (irsensors[IR.FrontRR.value])


        :return: (dictionary) A dictionary returning the values of all the IR sensors of the base. \
                 Dictionary keys: (string) IR ids (see :class:`~utils.IR`). \
                 Dictionary values: (float) The value of the IR.
        """
        return self.rem.state.irs

    def readColorBlob(self, color):
        """
        Reads the last detected blob of color of the indicated color
         
        :param color: (string) Color of the blob, one of the following: 'red','green','blue','custom'
        :return:  (Blob) A Blob object (see :class:`~utils.Blob`)  
        """
        return self.rem.state.blobs[color]

    def readAllColorBlobs(self):
        """
        Reads all the color blob data.

        :return: (dictionary) A dictionary returning the individual blob information. \
                 Dictionary keys: 'red', 'green', 'blue', 'custom'. Dictionary Values: Blob object (see :class:`~utils.Blob`)
        """
        return self.rem.state.blobs

    def readQR(self):
        return self.rem.state.qr

    def readOrientationSensor(self):
        """
        Reads the orientation sensor.

        *Warning*: This sensor may not be available on all the devices

        :return: (Orientation) An orientation object (see :class:`~utils.Orientation`)
        """
        return Orientation(self.rem.state.yaw, self.rem.state.pitch, self.rem.state.roll)

    def readAccelerationSensor(self):
        """
        Reads the acceleration sensor

        :return: (Acceleration) An Acceleration object (see :class:`~utils.Acceleration`)
        """
        return Acceleration(self.rem.state.accelx, self.rem.state.accely, self.rem.state.accelz)

    def readTapSensor(self):
        """
        Reads the data on the tap sensor

        :return: (Tap) A Tap object (see :class:`~utils.Tap`)
        """
        return Tap(self.rem.state.tapx, self.rem.state.tapy)

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
        """
        Returns the battery level of the base or the smartphone.

        :param device: (string) One of 'base' or 'phone'
        :return: (int) The battery level of the base or the smartphone
        """
        if device == "phone":
            return self.rem.state.phoneBattery
        else:
            return self.rem.state.baseBattery

    def readNoiseLevel(self):
        return self.rem.state.noise

    def readBrightnessSensor(self):
        """
        Reads the brightness detected by the smartphone light sensor

        :return: (int) The current brightness value
        """
        return self.rem.state.brightness

    def readFaceSensor(self):
        """
        Returns the position and distance of the last face detected by the robot.

        Example of use:

        .. code-block:: python

           face = robobo.readFaceSensor()
           print(face.distance)  #the distance to the person
           print(face.posX) # the position of the face in X axis
           print(fase.posY) # the position of the face in Y axis

        :return: (Face) A Face object (see :class:`~utils.Face`)

        """
        return self.rem.state.face

    def whenClapIsDetected(self, callback):
        """
        Configures the callback that is called when a new clap is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setClapCallback(callback)

    def whenANoteIsDetected(self, callback):
        """
        Configures the callback that is called when a new note is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setNoteCallback(callback)

    def whenANewFaceIsDetected(self, callback):
        """
        Configures the callback that is called when a new face is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        """
        Configures the callback that is called when a new color blob is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a new QR is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setNewQRCallback(callback)

    def whenATapIsDetected(self, callback):
        """
        Configures the callback that is called when a new tap is detected

        :param callback: (fun) The callback function to be called
        """

        self.rem.setTapCallback(callback)

    def whenAFlingIsDetected(self, callback):
        """
        Configures the callback that is called when a new fling is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setFlingCallback(callback)

    def whenAFaceIsLost(self, callback):
        """
        Configures the callback that is called when a face is lost

        :param callback: (fun) The callback function to be called
        """
        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a QR is detected

        :param callback: (fun) The callback function to be called
        """
        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        """
        Configures the callback that is called when a QR is lost

        :param callback: (fun) The callback function to be called
        """
        self.rem.setLostQRCallback(callback)

    def changeStatusFrequency(self, frequency):
        """
        Changes the frequency of the status messages coming from the robot.
        Status messages are filtered by default in order to reduce network bandwidth,
        a higher frequency reduces the filters.

        :param frequency: (StatusFrequency)
        """
        self.rem.changeStatusFrequency(frequency)

