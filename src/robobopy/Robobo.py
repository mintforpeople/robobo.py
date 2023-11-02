from robobopy.remotelib import Remote
from robobopy.utils.Wheels import Wheels
from robobopy.utils.Note import Note
from robobopy.utils.Acceleration import Acceleration
from robobopy.utils.Orientation import Orientation
from robobopy.utils.Tap import Tap
import time
from copy import copy, deepcopy

class Robobo:


    def __init__(self, ip, robot_id=0):
        """
        Creates a new Robobo library instance.

        :param ip: The IP address of the Robobo robot.

        :type ip: string

        :param robot_id: Sequential ID of robots. Only used in multi-robot scenarios in simulation.

        :type robot_id: int
        """

        self.rem = Remote(ip, robot_id)

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
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode. For more information, see: :ref:`blocking`.

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

        :param degrees: Position in degress of the PAN [-160..160]. See: :ref:`pan`.
        :param speed: Speed factor for the movement [0..100]. 100 is the maximum speed reachable, while 0 means no movement.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode. For more information, see: :ref:`blocking`.

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

        :param degrees: Position in degrees of the TILT [5..105]. See: :ref:`tilt`.
        :param speed: Speed factor for the movement [0..100]. 100 is the maximum speed reachable, while 0 means no movement.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode. For more information, see: :ref:`blocking`.
            
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

        :param note: Note to play index following the Anglo-Saxon notation, allowing 133 possible notes. The following scheme shows the equivalency in the range 48 to 59:

        ====  ==== ====  ==== ====  ====  ==== ==== ==== ====  ====  ====
        DO    DO#  RE    RE#  MI    FA    FA#  SOL  SOL# LA    LA#   SI
        C     Cs   D     Ds   E     F     Fs   G    Gs   A     As    B
        48    49   50    51   52    53    54   55   56   57    58    59
        ====  ==== ====  ==== ====  ====  ==== ==== ==== ====  ====  ====

        :param duration: Duration of the note in seconds (>0). Decimals like 0.2 are allowed.
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode. For more information, see: :ref:`blocking`.

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
        :param wait: If true, the instruction is executed in blocking mode. If false, it's executed in non-blocking mode. For more information, see: :ref:`blocking`.

        :type speech: string
        :type wait: bool
        """

        self.rem.talk(speech, wait)

    def setStreamFps(self, fps):
        """
        | Sets the stream fps. These are the number of frames per second sent from the smartphone to the computer. Default value is 60, buf effective value is usually lower (around 20), depending on the smartphone.
        | This change is persistent (see: :ref:`persistent`).

        :param fps: New upper limit of the stream fps. Takes positive values.

        :type fps: int

        """
        self.rem.setStreamFps(fps)

    def setCameraFps(self, fps):
        """
        | Sets the camera fps. These are the number of frames per second read by the smartphone camera. Default value is 60, buf effective value is usually lower (around 20), depending on the smartphone.
        | This change is persistent (see: :ref:`persistent`).

        :param fps: New upper limit of the camera fps. Takes positive values.

        :type fps: int
        """

        self.rem.setCameraFps(fps)

    def setFrontCamera(self):
        """
        | Makes Robobo use the frontal camera.
        | This change is persistent (see: :ref:`persistent`).
        """

        self.rem.setCamera("front")

    def setBackCamera(self):
        """
        | Makes Robobo use the back camera.
        | This change is persistent (see: :ref:`persistent`).
        """

        self.rem.setCamera("back")

    def startStream(self):
        """
        | Starts the camera streaming.
        | Camera streaming is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | In order to use this function, it's neccesary to download the project and follow the instructions from the `stream repository <https://github.com/mintforpeople/robobo-python-video-stream>`_.
        
        """

        self.rem.startStream()

    def stopStream(self):
        """
        | Stops the camera streaming.
        | Camera streaming is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        """

        self.rem.stopStream()

    def setAudioStreamBitrate(self, bitrate):
        """
        | Sets the audio stream bitrate. Audio bitrate is the measure of bits (audio data) processed over a given period of time and sent from the smartphone to the computer.
        | Default value is 44100 but it can be set to 22050, 44100, 48000, 96000, 192000. Higher means more audio quality but can cause latency problems. Some smartphones only support 44100 and 48000.
        | This change is persistent (see: :ref:`persistent`).

        :param bitrate: New bitrate value. Takes discrete values from the list [22050, 44100, 48000, 96000, 192000]

        :type bitrate: int

        """
        self.rem.setAudioStreamBitrate(bitrate)
    
    def startAudioStream(self):
        """
        | Starts the microphone streaming.
        | Microphone streaming is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | In order to use this function, it's neccesary to download the project and follow the instructions from the `stream repository <https://github.com/mintforpeople/robobo-python-audio-stream>`_.
        
        """

        self.rem.startAudioStream()

    def stopAudioStream(self):
        """
        | Stops the microphone streaming.
        | Audio streaming is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        """

        self.rem.stopAudioStream()

    def startFaceDetection(self):
        """
        | Starts the face detection.
        | Face detection is started by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopFaceDetection`, :class:`~Robobo.readFaceSensor`, :class:`~Robobo.resetFaceSensor`, :class:`~Robobo.whenAFaceIsLost`, :class:`~Robobo.whenANewFaceIsDetected`.
        """ 
        self.rem.startFaceDetection()

    def stopFaceDetection(self):
        """
        | Stops the face detection.
        | Face detection is started by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startFaceDetection`.
        """ 
        self.rem.stopFaceDetection()

    def startObjectRecognition(self):
        """
        | Starts the object recognition.
        | Object recognition is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopObjectRecognition`, :class:`~Robobo.readDetectedObject`, :class:`~Robobo.whenAnObjectIsDetected`.        
        | For more information, check the `Object Recognition Wiki <https://github.com/mintforpeople/robobo-programming/wiki/Real-time-object-identification>`_.
        """

        self.rem.startObjectRecognition()

    def stopObjectRecognition(self):
        """
        | Stops the object recognition.
        | Object recognition is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startObjectRecognition`.
        """

        self.rem.stopObjectRecognition()

    def startQrTracking(self):
        """
        | Starts the QR tracking.
        | QR tracking is started by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopQrTracking`, :class:`~Robobo.readQR`, :class:`~Robobo.whenANewQRCodeIsDetected`, :class:`~Robobo.whenAQRCodeIsDetected`, :class:`~Robobo.whenAQRCodeIsLost`.
        """

        self.rem.startQrTracking()

    def stopQrTracking(self):
        """
        | Stops the QR tracking.
        | QR tracking is started by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startQrTracking`.
        """

        self.rem.stopQrTracking()

    def startArUcoTagDetection(self):
        """
        | Starts the ArUcoTag detection.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopArUcoTagDetection`, :class:`~Robobo.setArucoTagSize`, :class:`~Robobo.readArucoTag`, :class:`~Robobo.whenArucoTagIsDetected`.
        | For more information, check the `ArUco Tag Detection Wiki <https://github.com/mintforpeople/robobo-programming/wiki/ArUco-marker-detection>`_.
        """

        self.rem.startTag()

    def setArucoTagSize(self, size):
        """
        | Sets the length of the side of the ArUco tag to be detected. It is important that this value fits the real tag size used, because it is used to calculate the distance from Robobo to the tag.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startArUcoTagDetection`.

        :param size: Size of the side of the ArUco tag in milimiters.

        :type size: int
        """

        self.rem.changeTagSize(size)

    def stopArUcoTagDetection(self):
        """
        | Stops the ArUco tag detection.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startArUcoTagDetection`.
        """

        self.rem.stopTag()

    def startLaneDetection(self):
        """
        | Starts the lane detection.
        | Lane detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopLaneDetection`, :class:`~Robobo.setLaneColorInversion`, :class:`~Robobo.readLaneBasic`, :class:`~Robobo.readLanePro`, :class:`~Robobo.whenALaneBasicDetected`, :class:`~Robobo.whenALaneProDetected`.
        | For more information, check the `Lane Detection Wiki <https://github.com/mintforpeople/robobo-programming/wiki/Lane-detection-library>`_.
        """

        self.rem.startLane()

    def stopLaneDetection(self):
        """
        | Stops the lane detection.
        | Lane detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startLaneDetection`.
        
        """

        self.rem.stopLane()

    def startLineDetection(self):
        """
        | Starts the line detection.
        | Line detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~utils.Lines.Lines`, :class:`~Robobo.stopLineDetection`, :class:`~Robobo.readLine`, :class:`~Robobo.whenALineIsDetected`.
        """

        self.rem.startLine()

    def stopLineDetection(self):
        """
        | Stops the line detection.
        | Line detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startLineDetection`.
        """

        self.rem.stopLine()

    def setLaneColorInversion(self, set_on):
        """
        | Toggles the color inversion for the advanced lane module. Usually, light lanes are detected against a dark background, but it is also possible to detect dark lanes against light backgrounds.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startLaneDetection`.

        :param set_on: Boolean to choose if turn it on or off.

        :type set_on: bool
        """

        if set_on:
            self.rem.setLaneColorInversionOn()
        else:
            self.rem.setLaneColorInversionOff()
    
    def startSpeechDetection(self):
        """
        | Starts the speech detection.
        | Speech detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        """

        self.rem.startSpeechDetection()

    def stopSpeechDetection(self):
        """
        | Stops the speech detection.
        | Speech detection is stopped by default.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.stopSpeechDetection`.
        """

        self.rem.stopSpeechDetection()
    
    def setSpeechDetectionPhraseOnly(self, set_on):
        """
        | Toggles the Speech Detection mode to only detect the registered phrases if true or anything if false
        | Registered phrases won't get cleared if this is toggled off
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startSpeechDetection`.

        :param set_on: Boolean to choose if turn it on or off.

        :type set_on: bool
        """

        if set_on:
            self.rem.detectSpeechPhrasesOnly()
        else:
            self.rem.detectAnySpeech()

    def registerSpeechDetectionPhrase(self, phrase):
        """
        | Registers a new phrase to be detected by the speech detection module
        | Registered phrases can be retrieved with :class:`~Robobo.readRegisteredSpeechPhrases`.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startSpeechDetection`.

        :param phrase: Phrase string to be registered.

        :type phrase: string
        """

        self.rem.registerSpeechPhrase(phrase)

    def removeSpeechDetectionPhrase(self, phrase):
        """
        | Removes a a phrase from the registered on the speech detection module. Has no effect if the phrase wasn't registered previously
        | Registered phrases can be retrieved with :class:`~Robobo.readRegisteredSpeechPhrases`.
        | This change is persistent (see: :ref:`persistent`).
        | See also: :class:`~Robobo.startSpeechDetection`.

        :param phrase: Phrase string to be removed.

        :type phrase: string
        """

        self.rem.removeSpeechPhrase(phrase)

    def startCamera(self):
        """
        Starts the camera.
        """

        self.rem.startCamera()

    def stopCamera(self):
        """
        | Stops the camera.
        | **Warning**: Other modules depend on the camera, so it's necessary to start it again to make use of them.

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
        | Resets the color blob detector. This sets to 0 the attributes of the last color blobs detected, but keeps the enabled and disabled colors the same.
        | See also: :class:`~Robobo.setActiveBlobs`.

        """

        self.rem.resetBlobs()

    def resetFaceSensor(self):
        """
        | Resets the face sensor. After this function, and until a new face is detected, the face sensor will return 0 for each attribute of the face object.
        | See also: :class:`~Robobo.startFaceDetection`.
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
        | **Note**: Before tracking blobs, it is highly recommended to follow the `camera calibration tutorial <https://github.com/mintforpeople/robobo-programming/wiki/camera-calibration-tutorial_en>`_.
        | Enables or disables the individual tracking of each color.
        | By default, green tracking is enabled and the rest are disabled.
        | **Warning**: Color tracking is a computationally intensive task, activating all the colors may impact performance.
        | See also: :class:`~Robobo.readAllColorBlobs`, :class:`~Robobo.readColorBlob`, :class:`~Robobo.resetColorBlobs`, :class:`~Robobo.whenANewColorBlobIsDetected`.

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
        | Sets advanced parameters for the blob tracker.

        | **Warning**: Only use this function if you know what you are doing. A bad configuration might have unexpected consecuences.

        :param frames: Number of frames passed to consider a blob lost.
        :param minarea: Minimum area to consdider a Blob as a Blob.
        :param max_count: max_count parameter of the termcriteria.
        :param epsilon: epsilon parameter of the termcriteria.

        :type frames: int
        :type minarea: int
        :type max_count: int
        :type epsilon: int
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
        Reads the current value sensed by the specified IR.
        This value depends on the distance to nearby objects, being larger for shorter distances.
        This value also depends on ambient conditions, such as the lighting.

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

        return deepcopy(self.rem.state.irs)

    def readColorBlob(self, color):
        """
        | Reads the last detected blob of the indicated color.
        | See also: :class:`~Robobo.setActiveBlobs`.
         
        :param color: Color of the blob.
        :type color: BlobColor

        :return:  The blob read.
        :rtype: Blob
        """

        return deepcopy(self.rem.state.blobs[color.value])

    def readAllColorBlobs(self):
        """
        | Reads all the color blob data.
        | See also: :class:`~Robobo.setActiveBlobs`.

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
                Dictionary keys (:class:`~utils.BlobColor`): the possible colors. Dictionary values (:class:`~utils.Blob`): the blobs.

        :rtype: dict
        """

        return deepcopy(self.rem.state.blobs)

    def readQR(self):
        """
        | Reads the last detected QR code.
        | See also: :class:`~Robobo.startQrTracking`.

        :return: The QR code read.

        :rtype: QRCode
        """

        return deepcopy(self.rem.state.qr)

    def readLine(self):
        """
        | Reads the last detected line.
        | See also: :class:`~Robobo.startLineDetection`.

        :return: The line read.

        :rtype: Lines       
        """

        return deepcopy(self.rem.state.lines)

    def readLaneBasic(self):
        """
        | Reads the last detected basic lane (straight lines).
        | See also: :class:`~Robobo.startLaneDetection`.

        :return: The lane read.

        :rtype: LaneBasic        
        """

        return deepcopy(self.rem.state.laneBasic)

    def readLanePro(self):
        """
        | Reads the last detected pro lane (Degree 2 polynomials).
        | See also: :class:`~Robobo.startLaneDetection`.

        :return: The pro lane read.
        
        :rtype: LanePro        
        """

        return deepcopy(self.rem.state.lanePro)

    def readOrientationSensor(self):
        """
        | Reads the orientation sensor.

        | **Warning**: This sensor may not be available on all the devices.

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

        :return: The position in degrees, taking values in range [-160..160]. See: :ref:`pan`.

        :rtype: int
        """

        return self.rem.state.panPos

    def readPanLastTime(self):
        """
                Returns the timestamp of the last received
                pan status

                :return: Time in milliseconds
                :rtype: int
                """
        return self.rem.state.lastPanTimestamp

    def readTiltPosition(self):
        """
        Reads the current position of the TILT.

        :return: The position in degrees, taking values in range [5..105]. See: :ref:`tilt`.

        :rtype: int
        """
        return self.rem.state.tiltPos

    def readTiltLastTime(self):
        """
                Returns the timestamp of the last received
                tilt status

                :return: Time in milliseconds
                :rtype: int
                """
        return self.rem.state.lastTiltTimestamp

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

    def readWheelLastTime(self):
        """
                Returns the timestamp of the last received
                wheel status

                :return: Time in milliseconds
                :rtype: int
                """
        return self.rem.state.lastWheelsTimestamp

    def readFlingAngle(self):
        """
        Reads the last angle detected on the fling sensor. This angle is formed by a horizontal line and the first and last points where the finger touched the screen.

        :return: The angle detected in degrees.

        :rtype: int
        """

        return self.rem.state.flingAngle

    def readFlingDistance(self):
        """
        Reads the length of the last fling detected by Robobo.

        :return: The length of the fling in pixels.
        :rtype: float
        """
        return self.rem.state.flingDistance

    def readFlingTime(self):
        """
        Reads the duration of the last fling detected by Robobo.

        :return: The duration of the fling in milliseconds.
        :rtype: float
        """

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
        """
        Reads the SPL (Sound Pressure Level) value, which is a measurement of the ambient noise.

        :return: The SPL value in decibels.

        :rtype: float
        """

        return self.rem.state.noise

    def readBrightnessSensor(self):
        """
        | Reads the ambient light level detected by the smartphone.
        | **Warning**: The light sensor may not be available on all the devices.

        :return: The brightness value in lux. It's a positive value.

        :rtype: int
        """

        return self.rem.state.brightness

    def readFaceSensor(self):
        """
        | Reads the last face detected by Robobo.
        | See also: :class:`~Robobo.startFaceDetection`.

        Example of use:

        .. code-block:: python

           face = robobo.readFaceSensor()
           print(face.distance)  #the distance to the person
           print(face.posX) # the position of the face in X axis
           print(fase.posY) # the position of the face in Y axis

        :return: The information of the face detected.
        :rtype: Face

        """
        return deepcopy(self.rem.state.face)

    def readArucoTag(self):
        """
        | Reads the last ArUco Tag detected by Robobo.
        | See also: :class:`~Robobo.startArUcoTagDetection`.

        :return: The Tag.

        :rtype: Tag
        """

        return deepcopy(self.rem.state.tag)

    def readDetectedObject(self):
        """
        | Reads the last object detected by Robobo.
        | See also: :class:`~Robobo.startObjectRecognition`.

        :return: The object.

        :rtype: DetectedObject
        """

        return deepcopy(self.rem.state.detectedObject)

    def readDetectedSpeech(self):
        """
        | Reads the last speech message detected by Robobo.
        | See also: :class:`~Robobo.startSpeechDetection`.

        :return: The object.

        :rtype: Speech
        """

        return deepcopy(self.rem.state.lastSpeech)
    
    def readRegisteredSpeechPhrases(self):
        """
        | Reads the list of registered speech phrases.
        | See also: :class:`~Robobo.startSpeechDetection`.

        :return: A list of registered string phrases.

        :rtype: list of str
        """

        return deepcopy(self.rem.state.registeredSpeechPhrases)

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
        | Configures the callback that is called when a new face is detected.
        | See also: :class:`~Robobo.startFaceDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        """
        | Configures the callback that is called when a new color blob is detected.
        | See also: :class:`~Robobo.setActiveBlobs`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        """
        | Configures the callback that is called when a new QR is detected. A QR is considered to be new if it's different to the last one detected.
        | See also: :class:`~Robobo.startQrTracking`.

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
        | Configures the callback that is called when a face is lost.
        | See also: :class:`~Robobo.startFaceDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        """
        | Configures the callback that is called when a QR is detected.
        | See also: :class:`~Robobo.startQrTracking`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        """
        | Configures the callback that is called when a QR is lost.
        | See also: :class:`~Robobo.startQrTracking`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLostQRCallback(callback)

    def whenArucoTagIsDetected(self, callback):
        """
        | Configures the callback that is called when a Tag is detected.
        | See also: :class:`~Robobo.startArUcoTagDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setTagCallback(callback)

    def whenAnObjectIsDetected(self, callback):
        """
        | Configures the callback that is called when an object is detected.
        | See also: :class:`~Robobo.startObjectRecognition`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setDetectedObjectCallback(callback)

    def whenALineIsDetected(self, callback):
        """
        | Configures the callback that is called when a line is detected.
        | See also: :class:`~Robobo.startLineDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLineCallback(callback)

    def whenALaneProDetected(self, callback):
        """
        | Configures the callback that is called when a pro lane is detected.
        | See also: :class:`~Robobo.startLaneDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """

        self.rem.setLaneProCallback(callback)

    def whenALaneBasicDetected(self, callback):
        """
        | Configures the callback that is called when a basic lane is detected.
        | See also: :class:`~Robobo.startLaneDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """
        
        self.rem.setLaneBasicCallback(callback)
    
    def whenSpeechDetected(self, callback):
        """
        | Configures the callback that is called when speech is detected.
        | See also: :class:`~Robobo.startSpeechDetection`.

        :param callback: The callback function to be called.

        :type callback: fun
        """
        
        self.rem.setSpeechDetectionCallback(callback)

    def setStatusFrequency(self, frequency):
        """
        | Sets the frequency of the status messages coming from Robobo. Status messages are filtered by default in order to reduce network bandwidth. A higher frequency reduces the filters, so more status messages are sent and more network bandwidth is used.
        | This change is persistent (see: :ref:`persistent`).

        :param frequency: New frequency of the status messages.

        :type frequency: StatusFrequency
        """
        
        self.rem.changeStatusFrequency(frequency)

    def sendSync(self, syncId):
        """
        Send a sync identifier to label the next frame sent through the camera stream

        :param syncId: Label to be applied to the frame
        :type syncId: int
        """
        self.rem.sendSync(syncId)
    
    def sendSyncAudio(self, syncId):
        """
        Send a sync identifier to label the next audio packet sent through the audio stream

        :param syncId: Label to be applied to the audio packet
        :type syncId: int
        """
        self.rem.sendSyncAudio(syncId)
    
