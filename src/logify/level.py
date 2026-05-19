from enum import Enum

class Level(Enum):
    ALL = -1
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5
    OFF = 1_000_000_000

    @classmethod
    def is_enabled(cls, threshold_level, event_level) -> bool:
        return event_level.value >= threshold_level.value
