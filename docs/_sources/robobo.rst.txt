
Robobo.py
==============

Robobo.py is the library used to create programs for the Robobo educational
robot in the Python language.

To create a Robobo instance:

.. code-block:: python

    from Robobo import Robobo

    rob = Robobo ('10.113.36.150')

**Parameters:**

- **ip:** (string) The IP address of the Robobo robot.

.. automodule:: Robobo
    :undoc-members:
    :show-inheritance:

    ==================
    Connection methods
    ==================

    .. automethod:: Robobo.connect
    .. automethod:: Robobo.disconnect

    ======================
    Base actuation methods
    ======================

    .. automethod:: Robobo.moveWheels
    .. automethod:: Robobo.moveWheelsByTime
    .. automethod:: Robobo.moveWheelsByDegrees
    .. automethod:: Robobo.stopMotors
    .. automethod:: Robobo.movePanTo
    .. automethod:: Robobo.moveTiltTo
    .. automethod:: Robobo.setLedColorTo

    ====================
    Base sensing methods
    ====================

    .. automethod:: Robobo.readBatteryLevel
    .. automethod:: Robobo.readIRSensor
    .. automethod:: Robobo.readAllIRSensor
    .. automethod:: Robobo.readWheelPosition
    .. automethod:: Robobo.readWheelSpeed
    .. automethod:: Robobo.readPanPosition
    .. automethod:: Robobo.readTiltPosition
    .. automethod:: Robobo.resetWheelEncoders

    ============================
    Smartphone actuation methods
    ============================

    .. automethod:: Robobo.playNote
    .. automethod:: Robobo.playSound
    .. automethod:: Robobo.sayText
    .. automethod:: Robobo.setEmotionTo

    ==========================
    Smartphone sensing methods
    ==========================

    .. automethod:: Robobo.readBatteryLevel
    .. automethod:: Robobo.setStatusFrequency

    .. automethod:: Robobo.setStreamFps
    .. automethod:: Robobo.setCameraFps
    .. automethod:: Robobo.setFrontCamera
    .. automethod:: Robobo.setBackCamera
    .. automethod:: Robobo.startStream
    .. automethod:: Robobo.stopStream
    .. automethod:: Robobo.startCamera
    .. automethod:: Robobo.stopCamera
    .. automethod:: Robobo.readBrightnessSensor

    .. automethod:: Robobo.setActiveBlobs
    .. automethod:: Robobo.readColorBlob
    .. automethod:: Robobo.readAllColorBlobs
    .. automethod:: Robobo.resetColorBlobs
    .. automethod:: Robobo.whenANewColorBlobIsDetected
    .. automethod:: Robobo.setAdvancedLostBlobParameters

    .. automethod:: Robobo.startFaceDetection
    .. automethod:: Robobo.stopFaceDetection
    .. automethod:: Robobo.readFaceSensor
    .. automethod:: Robobo.whenAFaceIsLost
    .. automethod:: Robobo.whenANewFaceIsDetected
    .. automethod:: Robobo.resetFaceSensor

    .. automethod:: Robobo.startObjectRecognition
    .. automethod:: Robobo.stopObjectRecognition
    .. automethod:: Robobo.readDetectedObject
    .. automethod:: Robobo.whenAnObjectIsDetected

    .. automethod:: Robobo.readLastNote
    .. automethod:: Robobo.whenANoteIsDetected
    .. automethod:: Robobo.readClapCounter
    .. automethod:: Robobo.whenClapIsDetected
    .. automethod:: Robobo.resetClapCounter
    .. automethod:: Robobo.readNoiseLevel

    .. automethod:: Robobo.readFlingAngle
    .. automethod:: Robobo.readFlingDistance
    .. automethod:: Robobo.readFlingTime
    .. automethod:: Robobo.resetFlingSensor
    .. automethod:: Robobo.whenAFlingIsDetected

    .. automethod:: Robobo.readOrientationSensor
    .. automethod:: Robobo.readAccelerationSensor

    .. automethod:: Robobo.readTapSensor
    .. automethod:: Robobo.resetTapSensor
    .. automethod:: Robobo.whenATapIsDetected

    .. automethod:: Robobo.startLaneDetection
    .. automethod:: Robobo.stopLaneDetection
    .. automethod:: Robobo.readLaneBasic
    .. automethod:: Robobo.readLanePro    
    .. automethod:: Robobo.setLaneColorInversion
    .. automethod:: Robobo.whenALaneProDetected
    .. automethod:: Robobo.whenALaneBasicDetected

    .. automethod:: Robobo.startQrTracking
    .. automethod:: Robobo.stopQrTracking
    .. automethod:: Robobo.readQR
    .. automethod:: Robobo.whenAQRCodeIsDetected
    .. automethod:: Robobo.whenANewQRCodeIsDetected
    .. automethod:: Robobo.whenAQRCodeIsLost

    .. automethod:: Robobo.startArUcoTagDetection
    .. automethod:: Robobo.setArucoTagSize
    .. automethod:: Robobo.stopArUcoTagDetection
    .. automethod:: Robobo.readArucoTags
    .. automethod:: Robobo.whenArucoTagIsDetected
    .. automethod:: Robobo.whenArucoTagAppears
    .. automethod:: Robobo.whenArucoTagDisappears

    .. automethod:: Robobo.startLineDetection
    .. automethod:: Robobo.stopLineDetection
    .. automethod:: Robobo.readLine
    .. automethod:: Robobo.whenALineIsDetected

    .. automethod:: Robobo.Robobo.startAudioStream
    .. automethod:: Robobo.Robobo.stopAudioStream

    .. automethod:: Robobo.Robobo.startSpeechDetection
    .. automethod:: Robobo.Robobo.stopSpeechDetection
    .. automethod:: Robobo.Robobo.readDetectedSpeech
    .. automethod:: Robobo.Robobo.whenSpeechDetected
    .. automethod:: Robobo.Robobo.setSpeechDetectionPhraseOnly
    .. automethod:: Robobo.Robobo.registerSpeechDetectionPhrase
    .. automethod:: Robobo.Robobo.removeSpeechDetectionPhrase
    .. automethod:: Robobo.Robobo.readRegisteredSpeechPhrases

    =============
    Other methods
    =============

    .. automethod:: Robobo.wait
