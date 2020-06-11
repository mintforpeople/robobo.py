
# robobo.py

Robobo.py is the library used to create programs for the Robobo educational robot (http://www.theroboboproject.com) in the Python language.

## Installation

To use this library on your project, clone or download this repository and you can use it in two ways:

* Put your .py files inside of "robobo.py" folder, or
* Add the folder "robobo.py" in your project folder and add "robobo.py" to your path as it's shown below:

    ```python
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'robobo.py'))
    ```

The library runs with **Python 3** and it must be installed before using the library, which also depends on the **websocket-client** library, that must be installed.

```bash
pip install websocket-client
```

## Basic usage

In this section, you can find basic documentation to install and start using the Robobo.py library. For further information you can read the Robobo.py library reference (https://mintforpeople.github.io/robobo.py/index.html).

To use the library within your code you have first to import it and then create a instance of the Robobo class:

```python
# This imports the library
from Robobo import Robobo

# This creates a instance of the Robobo class with the indicated ip address
robobo = Robobo('10.113.36.150')
```

After the library is instantiated, we can connect to the robot via the `connect()` method of the class

``` python
# This connects to the robobo base
robobo.connect()
```

When the robot is connected we can start to execute command on it.
There are 5 types of methods in the library, connection functions, like the ones that we talked before, commands to use the actuators of the robot, such as the wheels or the pan/tilt, methods to recover the status of the sensors, reset functions to clean the sensor values and callback setters to react to events in real time.

### Conection Methods

The connection methods are used to manage the connection with the robot:

```python
# Establishes a remote connection with the Robobo indicated by
# the IP address associated to this instance.
connect()

# Disconnects the library from the Robobo robot
disconnect()
```

### Actuator methods

The functions for controlling the effectors on the robot are the following:

```python
#Stops the movement of the wheels
stopMotors()

# Starts moving the wheels of the robot at the specified speed.
moveWheels(speedR, speedL)

"""
Moves the wheels of the robot at the specified speeds during the specified time.
  - If wait = True: (default value) It waits until the movement finishes.
  - If wait = False: the movement starts and the execution of the following command is
   immediately launched. This implies that the robot can execute the movement of another motor
   while the wheels are running.
"""
moveWheelsByTime(speedR, speedL, time, wait=True)

"""
Moves the PAN of the base to the specified position at the specified speed.
- If wait = True: (default value) It waits until the movement finishes.
- If wait = False: the movement starts and the execution of the following command is
  immediately launched.
"""
movePanTo(position, speed, wait=True)


"""
Moves the TILT of the base to the specified position at the specified speed.
- If wait = True: (default value) It waits until the movement finishes.
- If wait = False: The movement starts and the execution of the following command is
  immediately launched.
"""
moveTiltTo(position, speed, wait = True)


# Changes the color of a LED of the base*/
setLedColorTo(led, color)

# Changes the emotion of showed by the face of Robobo
setEmotionTo(emotion)

"""
Commands the robot to say the specified text
- If wait = True: (default value) It waits until the robots finishes reading the text
- If wait = False: It starts reading the text and the execution of the following command is
  immediately launched.
"""
sayText(text, wait = True)

# Commands the robot to play the specified emotion sound
playSound(sound)

"""
Commands the robot to play a musical note.
- If wait = True: (default value) It waits until the robots finishes
- If wait = False: It starts playing the note and the execution of the following command is
  immediately launched.
"""
playNote(note, time, wait = True)
```

Next we will see a simple program example:
In this example the robot will move the pan and tilt at the same time, and move forward, wait until the forward
movement is completed, say "Hello world" wait until the speech is completed, and move back.

```python
#This imports the library
from Robobo import Robobo

#This creates a instance of the Robobo class with the indicated ip address
robobo = Robobo('10.113.36.150')

# Connect to the robobo base
robobo.connect()

# Move pan and tilt and wheels and wait for the weels to complete
robobo.movePanTo(100, 20)
robobo.moveTiltTo(110, 20)
robobo.moveWheelsByTime(40, 40, 3)

# Say text and wait to finish
robobo.sayText("Hello world")

# Move robot
robobo.moveWheelsByTime(-40, -40, 3)
```

### Sensor methods

The sensor methods are used to retrieve the information from the different sensors of the robobo platform.

```python
# Returns the position of the wheel in degrees
readWheelPosition(wheel)

# Returns the current speed of the wheel
readWheelSpeed(wheel)

# Returns the current position of the PAN
readPanPosition()

# Returns the current position of the TILT
readTiltPosition()

# Returns the current value sensed by the specified IR
readIRSensor(sensor)

"""
Returns the values of all the IR sensors.
Example of use:

    irs = rob.readAllIRSensor()
    if irs != []:
        print (irs[IR.FrontR.value])
        print (irs[IR.FrontRR.value])     
"""
readAllIRSensor() 

# Returns the battery level of the base or the smartphone
readBatteryLevel(device) 


"""
Returns the position and distance of the last face detected by the robot.

Example of use:

   face = robobo.readFaceSensor()
   print(face.distance)  #the distance to the person
   print(face.posX) # the position of the face in X axis
   print(fase.posY) # the position of the face in Y axis
"""
readFaceSensor()

# Returns the number of claps registered since the last reset
readClapCounter() 

# Returns the last note detected by the note sensor
readLastNote() 

# Reads the last detected blob of color of the indicated color
readColorBlob(color)

# Reads all the color blob data
readAllColorBlobs()

# Returns the last note detected by the note sensor 
readLastNote()

```
If you need to call this functions on a loop you must call either the `robobo.wait()` methods at least once per iteration. 
The following example shows the values of all sensors in real time:

```python
from Robobo import Robobo

robobo = Robobo('192.168.0.71')
robobo.connect()

while True:
    robobo.wait(0.1)
    robobo.print("SENSOR STATUS:")
    robobo.print("IR: "+str(robobo.readAllIRSensor()))
    robobo.print("Blob: "+str(robobo.readAllColorBlobs()))
    robobo.print("Face: "+str(robobo.readFaceSensor()))
    robobo.print("Acceleration: "+str(robobo.readAccelerationSensor()))
    robobo.print("Orientation: "+str(robobo.readOrientationSensor()))
    robobo.print("Claps: "+str(robobo.readClapCounter()))
    robobo.print("Fling: "+str(robobo.readFlingSensor()))
    robobo.print("Tap: "+str(robobo.readTapSensor()))
    robobo.print("Battery: "+str(robobo.readBatteryLevel()))
```

There are some methods that allow to clear the sensor readings to the default values:

```python
"""
Resets the face sensor.
After this function, and until a new face is detected, the face sensor 
will return 0 as values for distance, x and y position.
"""
resetFaceSensor()

# Resets the clap counter
resetClapCounter()

# Resets the color blob detector
resetColorBlobs()

# Resets the state of the Fling sensor
resetFlingSensor()

# Resets the tap sensor value
resetTapSensor() 

# Resets the last note registered by the note sensor
resetLastNote()
    
```

### Configuration methods

The configuration methods allow to configure different parameters of the robot:

```python
"""
Activates the individual tracking of each color.
Warning: Color tracking is a computationally intensive task, activating all the colors may impact performance
"""
setColorBlobDetectionActive(red, green, blue, custom)

# Changes the frequency of the status (LOW, NORMAL,HIGH, MAX)
changeStatusFrequency(freq)
```

### Callback methods

The last type of methods allow the user to set up callback functions that will be called when a especific event is triggered.

```python
# Configures the callback that is called when a new note is detected
whenANoteIsDetected(fun)

# Configures the callback that is called when a new face is detected
whenANewFaceIsDetected(fun)

# Configures the callback that is called when a face is lost
whenAFaceIsLost(fun)

# Configures the callback that is called when a new color blob is detected
whenANewColorBlobIsDetected(fun)

# Configures the callback that is called when a new tap is detected
whenATapIsDetected(fun)

# Configures the callback that is called when a new fling is detected
whenAFlingIsDetected(fun)
```
