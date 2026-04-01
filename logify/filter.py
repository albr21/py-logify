from logify.log_event import LogEvent

class Filter:
    """
    Filters allows for filtering messages based on custom criteria based on log
    events - independently of the standard log level filtering.
    All filters must inherit from this class and implement the `allow` method
    which takes a LogEvent and returns either the log event (to allow it)
    or None (to deny it).
    By default, the allow method is passthrough and returns the log event.
    """

    # @param name [str] The name of the filter, used for identification and management
    # @return [None] No return value
    def __init__(self, name: str) -> None:
        self.name = name

    # @param log_event [LogEvent] The log event to evaluate against the filter criteria
    # @return [LogEvent | None] The log event if it passes the filter, or None if it is filtered out
    def allow(self, log_event: LogEvent) -> LogEvent | None:
        return log_event
