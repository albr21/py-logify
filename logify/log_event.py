class LogEvent():
    """
    LogEvent represents a single logify event, encapsulating all relevant
    information about the it.
    """

    # @param logger_name [str] The name of the logger that generated the event
    # @param level [str] The log level (e.g., "DEBUG", "INFO", "ERROR")
    # @param message [str] The log message
    # @param time [str] The timestamp of the log event in ISO 8601 format
    # @param exception [Exception, nil] An optional exception associated with the log event
    # @param data [dict, nil] An optional dictionary of additional data to include with the log event
    # @return [None] No return value
    def __init__(self, *, logger_name, level, message, time, exception=None, data=None) -> None:
        self.logger_name = logger_name
        self.level = level
        self.message = message
        self.time = time
        self.exception = exception
        self.data = data