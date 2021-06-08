from enum import Enum


class Emotions(Enum):
    """
    Represents the list of emotions Robobo's face can show.

    .. image:: _static/emotions.jpg
        :scale: 80 %
        :alt: Image showing how Robobo looks for each emotion: happy, laughung, surprised, sad, angry, normal, sleeping, tired or afraid.
    """
    HAPPY = "happy"
    LAUGHING = "laughing"
    SURPRISED = "surprised"
    SAD = "sad"
    ANGRY = "angry"
    NORMAL = "normal"
    SLEEPING = "sleeping"
    TIRED = "tired"
    AFRAID = "afraid"
