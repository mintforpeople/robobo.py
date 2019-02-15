from enum import Enum


class Emotions(Enum):
    """
    Represents the list of emotions Robobo's face can show.

    .. image:: _static/emotions.jpg
        :scale: 80 %

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
