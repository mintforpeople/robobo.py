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