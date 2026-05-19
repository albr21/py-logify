from ..layout import Layout
from ..log_event import LogEvent

class Basic(Layout):
    """
    Basic layout class for formatting log events
    """

    # Format the log event into a string
    # @param log_event [LogEvent] The log event to format
    # @return [str] The formatted log message
    def format(self, log_event: LogEvent) -> str:
        return f"{log_event.time} [{str(log_event.level).ljust(5)}] -- {log_event.logger_name}: {log_event.message}\n"
