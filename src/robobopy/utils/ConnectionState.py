from enum import Enum


class ConnectionState(Enum):

    DISCONNECTED = 0,
    CONNECTING = 1,
    CONNECTED = 2,
    ERROR = 3
