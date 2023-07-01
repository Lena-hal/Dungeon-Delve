from enum import Enum
class gameStatus(Enum):
    # this status sets how the game should act
    ONLINE = 1
    OFFLINE = 2
    PAUSED = 3
    IDLE = 4
    ERROR = 5
