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
     robot in the Python language.

     To create a Robobo instance:

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

        :param seconds: Time in seconds (accepts decimals like 0.2)
        :type seconds: float

        """
        time.sleep(seconds)

    def moveWheelsByTime(self, rSpeed, lSpeed, duration, wait=True):
        """
        Moves the wheels of the robot at the specified speeds during the specified time.

        :param rSpeed: Speed factor for the right wheel [-100..100]
        :param lSpeed: Speed factor for the left wheel [-100..100]
        :param duration: Time duration of the movement in seconds
        :param wait:
            * If wait = True: (default value) it waits until the movement finishes.
            * If wait = False: the movement starts and the execution of the following command is \
              immediately launched. This implies that the robot can execute the movement of another motor \
              while the wheels are running.

        :type rSpeed: int
        :type lSpeed: int
        :type duration: int
        :type wait: bool


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
        :type rSpeed: int
        :type lSpeed: int

        """
        self.rem.moveWheels(rSpeed, lSpeed, 100000)

    def stopMotors(self):
        """
        Stops the movement of the wheels
        """
        self.rem.moveWheels(0, 0, 1)

    def moveWheelsByDegrees(self, wheel, degrees, speed):
        """
        Moves the wheels of the robot by some degress at the specified speed.

        :param wheel: Wheels to move, one value of the Wheels enumeration.
        :param degrees: Degrees to move the wheel
        :param speed: Speed factor for the right wheel [-100..100]
        :type wheel: Wheels
        :type degrees: int
        :type speed: int

        """
        self.rem.moveWheelsByDegreeWait(wheel, degrees, speed)

    def movePanTo(self, degrees, speed, wait=True):
        """
        Moves the PAN of the base to the specified position at the specified speed

        :param degrees: Position in degress of the PAN [-160..160]
        :param speed: Speed factor [0..100]
        :param wait: True: blocking mode, False: non-blocking mode
        :type degrees: int
        :type speed: int
        :type wait: bool

        """
        if wait:
            self.rem.movePanWait(degrees, speed)
        else:
            self.rem.movePan(degrees, speed)

    def moveTiltTo(self, degrees, speed, wait=True):
        """
        Moves the TILT of the base to the specified position at the specified speed

        :param degrees: Position in degrees of the TILT [5..105]
        :param speed: Speed factor [0..100]
        :param wait: True: blocking mode, False: non-blocking mode
        :type degrees: int
        :type speed: int
        :type wait: bool
        """
        if wait:
            self.rem.moveTiltWait(degrees, speed)
        else:
            self.rem.moveTilt(degrees, speed)

    def setLedColorTo(self, led, color):
        """
        Changes the color of a LED of the base

        :param led: One value of the LED enumeration.
        :param color: One value of the  Color enumeration.
        :type led: LED
        :type color: Color

        """
        self.rem.setLedColor(led, color)

    def resetWheelEncoders(self):
        """
        Resets the encoders of the wheels
        """
        self.rem.resetEncoders()

    def playNote(self, note, duration, wait=True):
        """
        Commands the robot to play a musical note

        :param note: Musical note index [48..72]. Anglo-Saxon notation is used and there are 25 possible notes with the following basic correspondence. Any integer between 48 and 72.
        :param duration: Duration of the note in seconds (decimals can be used to used, like 0.2 or 0.5)
        :param wait: True: blocking mode, False: non-blocking mode
        :type note: int
        :type duration: int
        :type wait: bool
        """
        self.rem.playNote(note, duration, wait)

    def playSound(self, sound):
        """
        Commands the robot to play the specified emotion sound

        :param sound: One value of the Sound enumeration.
        :type sound: Sounds
        """
        self.rem.playEmotionSound(sound)

    def sayText(self, speech, wait=True):
        """
        Commands the robot to say the specified text

        :param speech: The text to say
        :param wait: True: blocking mode, False: non-blocking mode
        :type speech: String
        :type wait: bool
        """
        self.rem.talk(speech, wait)

    def setStreamFps(self, fps):
        """
        Commands the robot to change the stream fps

        :param fps: Upper limit of the stream's fps
        :type fps: int
        """
        self.rem.setStreamFps(fps)

    def setCameraFps(self, fps):
        """
        Commands the robot to change the camera fps

        :param fps: Upper limit of the camera's fps
        :type fps: int
        """
        self.rem.setCameraFps(fps)

    def startStream(self):
        """
        Commands the robot to start the camera streaming
        """
        self.rem.startStream()

    def stopStream(self):
        """
        Commands the robot to stop the camera streaming
        """
        self.rem.stopStream()

    def startColorDetection(self):
        """
        Commands the robot to start the color detection
        """
        self.rem.startColorDetection()

    def stopColorDetection(self):
        """
        Commands the robot to stop the color detection
        """
        self.rem.stopColorDetection()

    def startColorMeasurement(self):
        """
        Commands the robot to start the color measurement
        """
        self.rem.startColorMeasurement()

    def stopColorMeasurement(self):
        """
        Commands the robot to stop the color measurement
        """
        self.rem.stopColorMeasurement()

    def startFaceDetection(self):
        """
        Commands the robot to start the face detection
        """
        self.rem.startFaceDetection()

    def stopFaceDetection(self):
        """
        Commands the robot to stop the face detection
        """
        self.rem.stopFaceDetection()

    def startObjectRecognition(self):
        """
        Commands the robot to start the object recognition
        """
        self.rem.startObjectRecognition()

    def stopObjectRecognition(self):
        """
        Commands the robot to stop the object recognition
        """
        self.rem.stopObjectRecognition()

    def startQrTracking(self):
        """
        Commands the robot to start the  QR tracking
        """
        self.rem.startQrTracking()

    def stopQrTracking(self):
        """
        Commands the robot to stop the QR tracking
        """
        self.rem.stopQrTracking()

    def startArUcoTagDetection(self):
        """
        Commands the robot to start the ArUcoTag detection
        """
        self.rem.startTag()

    def stopArUcoTagDetection(self):
        """
        Commands the robot to stop the ArucoTag detection
        """
        self.rem.stopTag()

    def startLaneDetection(self):
        """
        Commands the robot to start the lane detection
        """
        self.rem.startLane()

    def stopLaneDetection(self):
        """
        Commands the robot to stop the lane detection
        """
        self.rem.stopLane()

    def startLineDetection(self):
        """
        Commands the robot to start the line detection
        """
        self.rem.startLine()

    def stopLineDetection(self):
        """
        Commands the robot to stop the line detection
        """
        self.rem.stopLine()

    def startLineStats(self):
        """
        Commands the robot to start the line detection STATUS report
        """
        self.rem.startLineStats()

    def stopLineStats(self):
        """
        Commands the robot to stop the line detection STATUS report
        """
        self.rem.stopLineStats()

    def toggleLaneColorInversion(self):
        """
        Commands the robot to toggle the color inversion.
        NOTE: this does not affects the yellow detection.
        """
        self.rem.toggleLaneColorInversion()

    def startCamera(self):
        """
        Commands the robot to start the camera
        """
        self.rem.startCamera()

    def stopCamera(self):
        """
        Commands the robot to stop the camera
        """
        self.rem.stopCamera()

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

        :param emotion: One value of the Emotion enumeration
        :type emotion: Emotions

        """
        self.rem.setEmotionTo(emotion)

    def setActiveBlobs(self, red, green, blue, custom):
        """
        Activates the individual tracking of each color.

        **Warning**: Color tracking is a computationally intensive task, activating all the colors may impact performance

        :param red: Enables red blob tracking
        :param green: Enables green blob tracking
        :param blue: Enables blue blob tracking
        :param custom: Enables custom blob tracking
        :type red: bool
        :type green: bool
        :type blue: bool
        :type custom: bool
        """
        self.rem.configureBlobTracking(red, green, blue, custom)

    def readClapCounter(self):
        """
        Returns the number of claps registered since the last reset

        :return: Clap counter
        :rtype: int
        """
        return self.rem.state.claps

    def readLastNote(self):
        """
        Returns the last note detected by the note sensor

        :return: A Note object
        :rtype: Note
        """
        return Note(self.rem.state.lastNote, self.rem.state.lastNoteDuration)

    def readIRSensor(self, id):
        """
        Returns the current value sensed by the specified IR

        :param id: One value of the IR enumeration
        :return: the current value of the IR
        :type id: IR
        :rtype: int

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
                print (irs[IR.FrontR.value])
                print (irs[IR.FrontRR.value])

        :return: A dictionary returning the values of all the IR sensors of the base. \
                 Dictionary keys: (string) IR ids (see :class:`~utils.IR.IR`). \
                 Dictionary values: (float) The value of the IR.
        :rtype: dict
        """
        return self.rem.state.irs

    def readColorBlob(self, color):
        """
        Reads the last detected blob of color of the indicated color
         
        :param color: Color of the blob, one of the following: 'red','green','blue','custom'
        :type color: string
        :return:  A Blob object
        :rtype: Blob
        """
        return self.rem.state.blobs[color]

    def readAllColorBlobs(self):
        """
        Reads all the color blob data.

        Example of use:

        .. code-block:: python

            blobs = rob.readAllColorBlobs()
            for key in blobs:
                blob = blobs[key]
                print(blob.color)
                print(blob.posx)
                print(blob.posy)
                print(blob.size)

        :return: A dictionary returning the individual blob information. \
                 Dictionary keys: 'red', 'green', 'blue', 'custom'. Dictionary Values: Blob object (see :class:`~utils.Blob`)
        :rtype: dict
        """
        return self.rem.state.blobs

    def readQR(self):
        """
        Reads the last detected QR code

        :return: (QRCode) A QRCode object (see :class:`~utils.QRCode`)
        """
        return self.rem.state.qr

    def readLine(self):
        """
        Reads the last detected lines

        :return: (Lines) A Lines object (see :class:`~utils.Lines`)
        """
        return self.rem.state.lines

    def readLaneBasic(self):
        """
        Reads the last detected basic lane (straight lines)

        :return: (LaneBasic) A LaneBasic object (see :class:`~utils.Lanes.LaneBasic`)
        """
        return self.rem.state.laneBasic

    def readLanePro(self):
        """
        Reads the last detected pro lane (2nd degree polynomials)

        :return: (LanePro) A LanePro object (see :class:`~utils.Lanes.LanePro`)
        """
        return self.rem.state.lanePro

    def readOrientationSensor(self):
        """
        Reads the orientation sensor.

        *Warning*: This sensor may not be available on all the devices

        :return: An orientation object.
        :rtype: Orientation
        """
        return Orientation(self.rem.state.yaw, self.rem.state.pitch, self.rem.state.roll)

    def readAccelerationSensor(self):
        """
        Reads the acceleration sensor

        :return: An Acceleration object.
        :rtype: Acceleration
        """
        return Acceleration(self.rem.state.accelx, self.rem.state.accely, self.rem.state.accelz)

    def readTapSensor(self):
        """
        Reads the data on the tap sensor

        :return: A Tap object.
        :rtype: Tap
        """
        return Tap(self.rem.state.tapx, self.rem.state.tapy)

    def readPanPosition(self):
        """
        Returns the current position of the PAN

        :return: The current position of the pan
        :rtype: int
        """
        return self.rem.state.panPos

    def readTiltPosition(self):
        """
        Returns the current position of the TILT

        :return: The current position of the TILT
        :rtype: int
        """
        return self.rem.state.tiltPos

    def readWheelPosition(self, wheel):
        """
        Returns the position of the wheel in degrees

        :param wheel: One of Wheels.L or Wheels.R
        :type wheel: Wheels
        :return: The position of the wheel in degrees
        :rtype: int
        """
        if wheel == Wheels.R:
            return self.rem.state.wheelPosR
        elif wheel == Wheels.L:
            return self.rem.state.wheelPosL
        else:
            print("Wheel id not valid")
            return 0

    def readWheelSpeed(self, wheel):
        """
        Returns the current speed of the wheel

        :param wheel: One of Wheels.L or Wheels.R
        :type wheel: Wheels
        :return: The current speed of the wheel
        :rtype: int
        """
        if wheel == Wheels.R:
            return self.rem.state.wheelSpeedR
        elif wheel == Wheels.L:
            return self.rem.state.wheelSpeedL
        else:
            print("Wheel id not valid")
            return 0

    def readFlingAngle(self):
        """
        Returns the angle detected on the fling sensor

        :return: The last angle detected on the sensor.
        :rtype: int
        """
        return self.rem.state.flingAngle

    def readFlingDistance(self):
        return self.rem.state.flingDistance

    def readFlingTime(self):
        return self.rem.state.flingTime

    def readBatteryLevel(self, device):
        """
        Returns the battery level of the base or the smartphone.

        :param device: One of 'base' or 'phone'
        :type device: string
        :return: The battery level of the base or the smartphone
        :rtype: int
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

        :return: The current brightness value
        :rtype: int
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

        :return: A Face object
        :rtype: Face

        """
        return self.rem.state.face

    def readTag(self):
        """
        Returns the last ArUco Tag detected by the robot.

        :return: A Tag object
        :rtype: Tag

        """
        return self.rem.state.tag

    def readDetectedObject(self):
        """
        Returns the last object detected by the robot.

        :return: A DetectedObject object
        :rtype: DetectedObject

        """
        return self.rem.state.detectedObject

    def whenClapIsDetected(self, callback):
        """
        Configures the callback that is called when a new clap is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setClapCallback(callback)

    def whenANoteIsDetected(self, callback):
        """
        Configures the callback that is called when a new note is detected

        :param callback: (fun) The callback function to be called
        :type callback: fun

        """
        self.rem.setNoteCallback(callback)

    def whenANewFaceIsDetected(self, callback):
        """
        Configures the callback that is called when a new face is detected

        :param callback: The callback function to be called
        :type callback: fun

        """
        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        """
        Configures the callback that is called when a new color blob is detected

        :param callback: The callback function to be called
        :rtype callback: fun
        """
        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a new QR is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setNewQRCallback(callback)

    def whenATapIsDetected(self, callback):
        """
        Configures the callback that is called when a new tap is detected

        :param callback: The callback function to be called
        :type callback: fun
        """

        self.rem.setTapCallback(callback)

    def whenAFlingIsDetected(self, callback):
        """
        Configures the callback that is called when a new fling is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setFlingCallback(callback)

    def whenAFaceIsLost(self, callback):
        """
        Configures the callback that is called when a face is lost

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a QR is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        """
        Configures the callback that is called when a QR is lost

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setLostQRCallback(callback)

    def whenATagIsDetected(self, callback):
        """
        Configures the callback that is called when a Tag is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setTagCallback(callback)

    def whenAnObjectIsDetected(self, callback):
        """
        Configures the callback that is called when an object is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setDetectedObjectCallback(callback)

    def whenALineIsDetected(self, callback):
        """
        Configures the callback that is called when a line is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setLineCallback(callback)

    def whenALaneProDetected(self, callback):
        """
        Configures the callback that is called when a pro lane is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setLaneProCallback(callback)

    def whenALaneBasicDetected(self, callback):
        """
        Configures the callback that is called when a basic lane is detected

        :param callback: The callback function to be called
        :type callback: fun
        """
        self.rem.setLaneBasicCallback(callback)

    def changeStatusFrequency(self, frequency):
        """
        Changes the frequency of the status messages coming from the robot.
        Status messages are filtered by default in order to reduce network bandwidth,
        a higher frequency reduces the filters.

        :param frequency: One value of the StatusFrequency enumeration
        :type frequency: StatusFrequency
        """
        self.rem.changeStatusFrequency(frequency)
