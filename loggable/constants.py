from enum import IntEnum


class LoggingLevel(IntEnum):
    """Enum with the different log levels available"""

    """Information describing a critical problem that has occurred."""
    CRITICAL = 50
    """Information describing a fatal problem that has occurred (same as critical)."""
    FATAL = 50
    """Information describing a major problem that has occurred."""
    ERROR = 40
    """ Information describing a minor problem that has occurred."""
    WARNING = 30
    """ Information describing a minor problem that has occurred (same as warning)."""
    WARN = 30
    """General system information."""
    INFO = 20
    """Low level system information for debugging purposes."""
    DEBUG = 10
    """No log level."""
    NOTSET = 0
