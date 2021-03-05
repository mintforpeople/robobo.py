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

    - **ip:** (string) The IP address of the Robobo robot.
    """

    def __init__(self, ip):
        """
        Creates a new Robobo.js library instance.

        :param ip: The IP address of the Robobo robot.

        :type ip: string
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
        Pauses the program for the specified time. After that time, next instruction is executed.

        :param seconds: Time to wait in seconds (>0). Decimals like 0.2 are allowed.

        :type seconds: float
        """

        time.sleep(seconds)

    def moveWheelsByTime(self, rSpeed, lSpeed, duration, wait=True):
        """
        Moves Robobo wheels during the specified time, each one at the specified speed.

        :param rSpeed: Speed factor for the right wheel [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.
        :param lSpeed: Speed factor for the left wheel [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.
        :param duration: Duration of the movement in seconds (>0). Decimals like 0.2 are allowed.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode.

        :type rSpeed: int
        :type lSpeed: int
        :type duration: float
        :type wait: bool
        """

        if wait:
            self.rem.moveWheelsWait(rSpeed, lSpeed, duration)
        else:
            self.rem.moveWheels(rSpeed, lSpeed, duration)

    def moveWheels(self, rSpeed, lSpeed):
        """
        Moves Robobo wheels, each one at the specified speed.
        
        :param rSpeed: Speed factor for the right wheel [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.
        :param lSpeed: Speed factor for the left wheel [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.
        
        :type rSpeed: int
        :type lSpeed: int
        """

        self.rem.moveWheels(rSpeed, lSpeed, 100000)

    def stopMotors(self):
        """
        Stops the movement of the wheels.
        """

        self.rem.moveWheels(0, 0, 1)

    def moveWheelsByDegrees(self, wheel, degrees, speed):
        """
        Moves Robobo wheels by some degrees at the specified speed.

        :param wheel: Wheel or wheels to move.
        :param degrees: Degrees to move the wheel or wheels (>0).
        :param speed: Speed factor for the movement [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.

        :type wheel: Wheels
        :type degrees: int
        :type speed: int
        """
        
        self.rem.moveWheelsByDegreeWait(wheel, degrees, speed)

    def movePanTo(self, degrees, speed, wait=True):
        """
        Moves the PAN of the base to the specified position at the specified speed.

        :param degrees: Position in degress of the PAN [-160..160].
        :param speed: Speed factor for the movement [0..100]. 100 is the maximum speed reachable, while 0 means no movement.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode.

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
        Moves the TILT of the base to the specified position at the specified speed.

        :param degrees: Position in degrees of the TILT [5..105].
        :param speed: Speed factor for the movement [0..100]. 100 is the maximum speed reachable, while 0 means no movement.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode.
            
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
        Set the color of a LED of the base.

        :param led: LED to set the color of.
        :param color: New color of the LED.

        :type led: LED
        :type color: Color
        """

        self.rem.setLedColor(led, color)

    def resetWheelEncoders(self):
        """
        Resets the encoders of the wheels.
        """

        self.rem.resetEncoders()

    def playNote(self, note, duration, wait=True):
        """
        Makes Robobo play a musical note.

        :param note: Note to play index following the Anglo-Saxon notation [48..72].
        :param duration: Duration of the note in seconds (decimals like 0.2 are allowed).
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode.

        :type note: int
        :type duration: float
        :type wait: bool
        """

        self.rem.playNote(note, duration, wait)

    def playSound(self, sound):
        """
        Makes Robobo play the specified emotion sound.

        :param sound: The emotion sound to play.

        :type sound: Sounds
        """

        self.rem.playEmotionSound(sound)

    def sayText(self, speech, wait=True):
        """
        Makes Robobo say the specified text.

        :param speech: The text to say.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode.

        :type speech: string
        :type wait: bool
        """

        self.rem.talk(speech, wait)

    def setStreamFps(self, fps):
        """
        Sets the stream fps. These are the number of frames per second received from the smartphone camera.
        Changes are persistent.

        :param fps: New upper limit of the stream fps. Takes positive values, and the maximum value taken depends on the smartphone, but it is usually around 20.

        :type fps: int

        """
        self.rem.setStreamFps(fps)

    def setCameraFps(self, fps):
        """
        Sets the camera fps. These are the number of frames per second read by the smartphone camera.
        Changes are persistent.

        :param fps: New upper limit of the camera fps. Takes positive values, and the maximum value taken depends on the smartphone, but it is usually around 20.

        :type fps: int
        """

        self.rem.setCameraFps(fps)

    def setFrontCamera(self):
        """
        Makes Robobo use the frontal camera.
        """

        self.rem.setCamera("front")

    def setBackCamera(self):
        """
        Makes Robobo use the back camera.
        """

        self.rem.setCamera("back")

    def startStream(self):
        """
        Starts the camera streaming. Camera streaming is stopped by default. This change is persistant.
        """

        self.rem.startStream()

    def stopStream(self):
        """
        Stops the camera streaming. Camera streaming is stopped by default. This change is persistant.
        """

        self.rem.stopStream()

    def startFaceDetection(self):
        """
        Starts the face detection. Face detection is started by default. This change is persistant.
        """ 
        self.rem.startFaceDetection()

    def stopFaceDetection(self):
        """
        Stops the face detection. Face detection is started by default. This change is persistant.
        """ 
        self.rem.stopFaceDetection()

    def startObjectRecognition(self):
        """
        Starts the object recognition. Object recognition is stopped by default. This change is persistant.
        """

        self.rem.startObjectRecognition()

    def stopObjectRecognition(self):
        """
        Stops the object recognition. Object recognition is stopped by default. This change is persistant.
        """

        self.rem.stopObjectRecognition()

    def startQrTracking(self):
        """
        Starts the QR tracking. QR tracking is started by default. This change is persistant.
        """

        self.rem.startQrTracking()

    def stopQrTracking(self):
        """
        Stops the QR tracking. QR tracking is started by default. This change is persistant.
        """

        self.rem.stopQrTracking()

    def startArUcoTagDetection(self):
        """
        Starts the ArUcoTag detection.
        """

        self.rem.startTag()

    def setArucoTagSize(self, size):
        """
        Sets the length of the side of the ArUco tag to be detected. It is important that this value fits the real tag size used, because it is used to calculate the distance from Robobo to the tag.
        This change is persistent.

        :param size: Size of the side of the ArUco tag in milimiters.

        :type size: int
        """

        self.rem.changeTagSize(size)

    def stopArUcoTagDetection(self):
        """
        Stops the ArUco tag detection.
        """

        self.rem.stopTag()

    def startLaneDetection(self):
        """
        Starts the lane detection. Lane detection is stopped by default. This change is persistant.
        """

        self.rem.startLane()

    def stopLaneDetection(self):
        """
        Stops the lane detection. Lane detection is stopped by default. This change is persistant.
        """

        self.rem.stopLane()

    def startLineDetection(self):
        """
        Starts the line detection. Line detection is stopped by default. This change is persistant.
        """

        self.rem.startLine()

    def stopLineDetection(self):
        """
        Stops the line detection. Line detection is stopped by default. This change is persistant.
        """

        self.rem.stopLine()

    def setLaneColorInversion(self, set_on):
        """
        Toggles the color inversion for the advanced lane module. Usually, light lanes are detected against a dark background, but it is also possible to detect dark lanes against light backgrounds.
        Changes are persistent.

        :param set_on: Boolean to choose if turn it on or off.

        :type set_on: bool
        """

        if set_on:
            self.rem.setLaneColorInversionOn()
        else:
            self.rem.setLaneColorInversionOff()

    def startCamera(self):
        """
        Starts the camera.
        """

        self.rem.startCamera()

    def stopCamera(self):
        """
        Stops the camera.
        """

        self.rem.stopCamera()

    def resetClapCounter(self):
        """
        Resets the clap counter.
        """

        self.rem.resetClaps()

    def resetTapSensor(self):
        """
        Resets the tap sensor value.
        """

        self.rem.resetTap()

    def resetFlingSensor(self):
        """
        Resets the state of the Fling sensor.
        """

        self.rem.resetFling()

    def resetColorBlobs(self):
        """
        Resets the color blob detector. This sets to 0 the attributes of the last color blobs detected, but keeps the enabled and disabled colors the same.
        """

        self.rem.resetBlobs()

    def resetFaceSensor(self):
        """
        Resets the face sensor. After this function, and until a new face is detected, the face sensor will return 0 for each attribute of the face object.
        """

        self.rem.resetFace()

    def setEmotionTo(self, emotion):
        """
        Changes the emotion showed by the face of Robobo.

        :param emotion: New emotion to show.

        :type emotion: Emotions
        """

        self.rem.setEmotionTo(emotion)

    def setActiveBlobs(self, red, green, blue, custom):
        """
        Enables or disables the individual tracking of each color. By default, green tracking is enabled and the rest are disabled.

        **Warning**: Color tracking is a computationally intensive task, activating all the colors may impact performance.

        :param red: If true, enables red blob tracking.
        :param green: If true, enables green blob tracking.
        :param blue: If true, enables blue blob tracking.
        :param custom: If true, enables custom blob tracking.

        :type red: bool
        :type green: bool
        :type blue: bool
        :type custom: bool
        """

        self.rem.configureBlobTracking(red, green, blue, custom)

    def setAdvancedLostBlobParameters(self,  frames = 5, minarea = 1000, max_count = 1, epsilon = 0):
        """
        Sets advanced parameters for the blob tracker.

        **Warning**: Only use this function if you know what you are doing. A bad configuration might have unexpected consecuences.

        :param frames: Number of frames passed to consider a blob lost.
        :param minarea: Minimum area to consdider a Blob as a Blob.
        :param max_count: max_count parameter of the termcriteria.
        :param epsilon: epsilon parameter of the termcriteria.

        :type frames:int
        :type minarea: int
        :type max_count: int
        :type epsilon :int
        """

        self.rem.advancedLostBlobConfiguration(frames, minarea, max_count, epsilon)

    def readClapCounter(self):
        """
        Reads the number of claps registered since last reset.

        :return: The number of claps.

        :rtype: int
        """

        return self.rem.state.claps

    def readLastNote(self):
        """
        Reads the last note detected by the note sensor.

        :return: The note read.

        :rtype: Note
        """

        return Note(self.rem.state.lastNote, self.rem.state.lastNoteDuration)

    def readIRSensor(self, id):
        """
        Reads the current value sensed by the specified IR. This value depends on the distance to nearby objects, being larger for shorter distances. This value also depends on ambient conditions, such as the lighting.

        :param id: The IR to read the value sensed from.
        :return: The value of the IR read.

        :type id: IR
        :rtype: int
        """

        if self.rem.state.irs == []:
            return 0
        else:
            return int(self.rem.state.irs[id.value])

    def readAllIRSensor(self):
        """
        Reads the values of all the IR sensors.

        Example of use:

        .. code-block:: python

            irs = rob.readAllIRSensor()
            if irs != []:
                print (irs[IR.FrontR.value])
                print (irs[IR.FrontRR.value])

        :return: A dictionary returning the values of all the IR sensors of the base. \
                 Dictionary keys (string): IR ids (see :class:`~utils.IR.IR`). \
                 Dictionary values (float): The value of the IR.
        :rtype: dict
        """

        return self.rem.state.irs

    def readColorBlob(self, color):
        """
        Reads the last detected blob of the indicated color.
         
        :param color: Color of the blob, one of the following: 'red','green','blue','custom'.
        :type color: string

        :return:  The blob read.
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
                 Dictionary keys: 'red', 'green', 'blue', 'custom'. Dictionary values: Blob object (see :class:`~utils.Blob`).

        :rtype: dict
        """

        return self.rem.state.blobs

    def readQR(self):
        """
        Reads the last detected QR code.

        :return: The QR code read.

        :rtype: QRCode
        """

        return self.rem.state.qr

    def readLine(self):
        """
        Reads the last detected line.

        :return: The line read.

        :rtype: Lines       
        """

        return self.rem.state.lines

    def readLaneBasic(self):
        """
        Reads the last detected basic lane (straight lines).

        :return: The lane read.

        :rtype: LaneBasic        
        """

        return self.rem.state.laneBasic

    def readLanePro(self):
        """
        Reads the last detected pro lane (Degree 2 polynomials).

        :return: The pro lane read.
        
        :rtype: LanePro        
        """

        return self.rem.state.lanePro

    def readOrientationSensor(self):
        """
        Reads the orientation sensor.

        **Warning**: This sensor may not be available on all the devices.

        :return: The orientation read.

        :rtype: Orientation
        """

        return Orientation(self.rem.state.yaw, self.rem.state.pitch, self.rem.state.roll)

    def readAccelerationSensor(self):
        """
        Reads the acceleration sensor.

        :return: The acceleration read.

        :rtype: Acceleration
        """

        return Acceleration(self.rem.state.accelx, self.rem.state.accely, self.rem.state.accelz)

    def readTapSensor(self):
        """
        Reads the data on the tap sensor.

        :return: The data read.

        :rtype: Tap
        """

        return Tap(self.rem.state.tapx, self.rem.state.tapy)

    def readPanPosition(self):
        """
        Reads the current position of the PAN.

        :return: The position in degrees, taking values in range [-160..160].

        :rtype: int
        """

        return self.rem.state.panPos

    def readTiltPosition(self):
        """
        Reads the current position of the TILT.

        :return: The position in degrees, taking values in range [-90..90]

        :rtype: int
        """
        return self.rem.state.tiltPos

    def readWheelPosition(self, wheel):
        """
        Reads the current position of the specified wheel.

        :param wheel: The wheel to read the position of. One of Wheels.L or Wheels.R.
        :type wheel: Wheels

        :return: The position of the wheel in degrees.
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
        Returns the current speed of the specified wheel.

        :param wheel: The wheel to read the position of. One of Wheels.L or Wheels.R
        :type wheel: Wheels

        :return: The current speed of the wheel [-100..100]. Absolute value 100 is the maximum speed reachable, while 0 means no movement. Positive values mean the wheel moves forwards and negative values mean it moves backwards.
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
        Reads the last angle detected on the fling sensor.

        :return: The angle detected in degrees.

        :rtype: int
        """

        return self.rem.state.flingAngle

    def readFlingDistance(self):
        return self.rem.state.flingDistance

    def readFlingTime(self):
        return self.rem.state.flingTime

    def readBatteryLevel(self, device):
        """
        Reads the battery level of the base or the smartphone.

        :param device: One of 'base' or 'phone'.
        :type device: string

        :return: The battery level of the specified device.
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
        Reads the brightness detected by the smartphone light sensor.

        :return: The brightness value.

        :rtype: int
        """

        return self.rem.state.brightness

    def readFaceSensor(self):
        """
        Returns the position and distance of the last face detected by Robobo.

        Example of use:

        .. code-block:: python

           face = robobo.readFaceSensor()
           print(face.distance)  #the distance to the person
           print(face.posX) # the position of the face in X axis
           print(fase.posY) # the position of the face in Y axis

        :return: The information of the face detected.
        :rtype: Face

        """
        return self.rem.state.face

    def readArucoTag(self):
        """
        Reads the last ArUco Tag detected by Robobo.

        :return: The Tag.

        :rtype: Tag
        """

        return self.rem.state.tag

    def readDetectedObject(self):
        """
        Reads the last object detected by Robobo.

        :return: The object.

        :rtype: DetectedObject
        """

        return self.rem.state.detectedObject

    def whenClapIsDetected(self, callback):
        """
        Configures the callback that is called when a new clap is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setClapCallback(callback)

    def whenANoteIsDetected(self, callback):
        """
        Configures the callback that is called when a new note is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setNoteCallback(callback)

    def whenANewFaceIsDetected(self, callback):
        """
        Configures the callback that is called when a new face is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        """
        Configures the callback that is called when a new color blob is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a new QR is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setNewQRCallback(callback)

    def whenATapIsDetected(self, callback):
        """
        Configures the callback that is called when a new tap is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setTapCallback(callback)

    def whenAFlingIsDetected(self, callback):
        """
        Configures the callback that is called when a new fling is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setFlingCallback(callback)

    def whenAFaceIsLost(self, callback):
        """
        Configures the callback that is called when a face is lost.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        """
        Configures the callback that is called when a QR is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        """
        Configures the callback that is called when a QR is lost.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLostQRCallback(callback)

    def whenArucoTagIsDetected(self, callback):
        """
        Configures the callback that is called when a Tag is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setTagCallback(callback)

    def whenAnObjectIsDetected(self, callback):
        """
        Configures the callback that is called when an object is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setDetectedObjectCallback(callback)

    def whenALineIsDetected(self, callback):
        """
        Configures the callback that is called when a line is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLineCallback(callback)

    def whenALaneProDetected(self, callback):
        """
        Configures the callback that is called when a pro lane is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLaneProCallback(callback)

    def whenALaneBasicDetected(self, callback):
        """
        Configures the callback that is called when a basic lane is detected.

        :param callback: The callback function to be called.

        :type callback: fun
        """
        
        self.rem.setLaneBasicCallback(callback)

    def setStatusFrequency(self, frequency):
        """
        Sets the frequency of the status messages coming from Robobo.
        Status messages are filtered by default in order to reduce network bandwidth. A higher frequency reduces the filters, so more status messages are sent and more network bandwidth is used.
        This change is persistent.

        :param frequency: New frequency of the status messages.

        :type frequency: StatusFrequency
        """
        
        self.rem.changeStatusFrequency(frequency)
