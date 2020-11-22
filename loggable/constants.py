from enum import IntEnum


class LoggingLevel(IntEnum):
    """Enum of available log levels."""
    CRITICAL = 50
    FATAL = 50
    ERROR = 40
    WARNING = 30
    WARN = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0
