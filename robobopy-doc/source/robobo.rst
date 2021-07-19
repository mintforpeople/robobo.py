
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

    .. autofunction:: Robobo.Robobo.connect
    .. autofunction:: Robobo.Robobo.disconnect

    ======================
    Base actuation methods
    ======================

    .. autofunction:: Robobo.Robobo.moveWheels
    .. autofunction:: Robobo.Robobo.moveWheelsByTime
    .. autofunction:: Robobo.Robobo.moveWheelsByDegrees
    .. autofunction:: Robobo.Robobo.stopMotors
    .. autofunction:: Robobo.Robobo.movePanTo
    .. autofunction:: Robobo.Robobo.moveTiltTo
    .. autofunction:: Robobo.Robobo.setLedColorTo

    ====================
    Base sensing methods
    ====================

    .. autofunction:: Robobo.Robobo.readBatteryLevel
    .. autofunction:: Robobo.Robobo.readIRSensor
    .. autofunction:: Robobo.Robobo.readAllIRSensor
    .. autofunction:: Robobo.Robobo.readWheelPosition
    .. autofunction:: Robobo.Robobo.readWheelSpeed
    .. autofunction:: Robobo.Robobo.readPanPosition
    .. autofunction:: Robobo.Robobo.readTiltPosition
    .. autofunction:: Robobo.Robobo.resetWheelEncoders

    ============================
    Smartphone actuation methods
    ============================

    .. autofunction:: Robobo.Robobo.playNote
    .. autofunction:: Robobo.Robobo.playSound
    .. autofunction:: Robobo.Robobo.sayText
    .. autofunction:: Robobo.Robobo.setEmotionTo

    ==========================
    Smartphone sensing methods
    ==========================

    .. autofunction:: Robobo.Robobo.readBatteryLevel
    .. autofunction:: Robobo.Robobo.setStatusFrequency

    .. autofunction:: Robobo.Robobo.setStreamFps
    .. autofunction:: Robobo.Robobo.setCameraFps
    .. autofunction:: Robobo.Robobo.setFrontCamera
    .. autofunction:: Robobo.Robobo.setBackCamera
    .. autofunction:: Robobo.Robobo.startStream
    .. autofunction:: Robobo.Robobo.stopStream
    .. autofunction:: Robobo.Robobo.startCamera
    .. autofunction:: Robobo.Robobo.stopCamera
    .. autofunction:: Robobo.Robobo.readBrightnessSensor

    .. autofunction:: Robobo.Robobo.setActiveBlobs
    .. autofunction:: Robobo.Robobo.readColorBlob
    .. autofunction:: Robobo.Robobo.readAllColorBlobs
    .. autofunction:: Robobo.Robobo.resetColorBlobs
    .. autofunction:: Robobo.Robobo.whenANewColorBlobIsDetected
    .. autofunction:: Robobo.Robobo.setAdvancedLostBlobParameters

    .. autofunction:: Robobo.Robobo.startFaceDetection
    .. autofunction:: Robobo.Robobo.stopFaceDetection
    .. autofunction:: Robobo.Robobo.readFaceSensor
    .. autofunction:: Robobo.Robobo.whenAFaceIsLost
    .. autofunction:: Robobo.Robobo.whenANewFaceIsDetected
    .. autofunction:: Robobo.Robobo.resetFaceSensor

    .. autofunction:: Robobo.Robobo.startObjectRecognition
    .. autofunction:: Robobo.Robobo.stopObjectRecognition
    .. autofunction:: Robobo.Robobo.readDetectedObject
    .. autofunction:: Robobo.Robobo.whenAnObjectIsDetected

    .. autofunction:: Robobo.Robobo.readLastNote
    .. autofunction:: Robobo.Robobo.whenANoteIsDetected
    .. autofunction:: Robobo.Robobo.readClapCounter
    .. autofunction:: Robobo.Robobo.whenClapIsDetected
    .. autofunction:: Robobo.Robobo.resetClapCounter
    .. autofunction:: Robobo.Robobo.readNoiseLevel

    .. autofunction:: Robobo.Robobo.readFlingAngle
    .. autofunction:: Robobo.Robobo.readFlingDistance
    .. autofunction:: Robobo.Robobo.readFlingTime
    .. autofunction:: Robobo.Robobo.resetFlingSensor
    .. autofunction:: Robobo.Robobo.whenAFlingIsDetected

    .. autofunction:: Robobo.Robobo.readOrientationSensor
    .. autofunction:: Robobo.Robobo.readAccelerationSensor

    .. autofunction:: Robobo.Robobo.readTapSensor
    .. autofunction:: Robobo.Robobo.resetTapSensor
    .. autofunction:: Robobo.Robobo.whenATapIsDetected

    .. autofunction:: Robobo.Robobo.startLaneDetection
    .. autofunction:: Robobo.Robobo.stopLaneDetection
    .. autofunction:: Robobo.Robobo.readLaneBasic
    .. autofunction:: Robobo.Robobo.readLanePro    
    .. autofunction:: Robobo.Robobo.setLaneColorInversion
    .. autofunction:: Robobo.Robobo.whenALaneProDetected
    .. autofunction:: Robobo.Robobo.whenALaneBasicDetected

    .. autofunction:: Robobo.Robobo.startQrTracking
    .. autofunction:: Robobo.Robobo.stopQrTracking
    .. autofunction:: Robobo.Robobo.readQR
    .. autofunction:: Robobo.Robobo.whenAQRCodeIsDetected
    .. autofunction:: Robobo.Robobo.whenANewQRCodeIsDetected
    .. autofunction:: Robobo.Robobo.whenAQRCodeIsLost

    .. autofunction:: Robobo.Robobo.startArUcoTagDetection
    .. autofunction:: Robobo.Robobo.setArucoTagSize
    .. autofunction:: Robobo.Robobo.stopArUcoTagDetection
    .. autofunction:: Robobo.Robobo.readArucoTag
    .. autofunction:: Robobo.Robobo.whenArucoTagIsDetected

    .. autofunction:: Robobo.Robobo.startLineDetection
    .. autofunction:: Robobo.Robobo.stopLineDetection
    .. autofunction:: Robobo.Robobo.readLine
    .. autofunction:: Robobo.Robobo.whenALineIsDetected

    =============
    Other methods
    =============

    .. autofunction:: Robobo.Robobo.wait
