.. _features:

General features
================

In this section, some particularities of Robobo which are common to several functions and classes are explained.

.. _blocking:

Blocking instructions
---------------------

A blocking instruction prevents Robobo from executing other instructions until it has finished.
A non blocking instruction, once executed, allows other instructions to be executed simultaneously.
Some instructions can be executed both in blocking and non blocking mode.

.. _modules:

Enabled and disabled modules
----------------------------

For better performance, some modules are disabled by default. In order to use this modules, it's necessary to start them. After using this modules, it's recommended to stop them.
This are the modules enabled by default: face detection, color blob detection and QR tracking.
This are the modules disabled by default: camera stream, line detection, lane detection, object recognition, ArUco tag detection.

.. _screen:

Screen coordinates
------------------

Screen coordinates have their origin at the upper left corner of the screen.
The x axis follows the upper side of the screen, from left to right. It takes values between 0 and 100, being 0 the left side and 100 the right side of the screen.
The y axis follows the left side of the screen, from top to bottom. It takes values between 0 and 100, being 0 the upper side and 100 the lower side of the screen.

.. image:: _static/tap_position.jpg
    :alt: Image showing the two coordinate axes on the screen of the smartphone, which is showing Robobo face.


.. _persistent:

Persistent changes
------------------

Some of the functions called affect Robobo hardware.
Persistent changes remain even if the program finishes and until Robobo is restarted, when it takes all the default values again.

.. _tilt:

Tilt positions
--------------

The following image shows the different positions of the tilt, which can take angles between 5 and 105 degrees.

.. image:: _static/tilt.PNG
    :scale: 50 %
    :alt: Image showing standard smartphone position at 75 degrees, and indicating that lower values mean it rotated backwards while higher values mean it rotated forwards.

.. _pan:

Pan positions
--------------

The following image shows the different positions of the pan, which can take angles between -160 and 160 degrees.

.. image:: _static/pan.PNG
    :scale: 50 %
    :alt: Image showing standard smartphone position at 0 degrees, and indicating that lower values mean it rotated left while higher values mean it rotated right.