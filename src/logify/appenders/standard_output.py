from ..appender import Appender

class StandardOutput(Appender):
    """
    Appender that writes log events to the standard output.
    """

    # Write the log event
    # @param log_event [LogEvent] The log event to write
    # @return [None] No return value
    def write(self, log_event) -> None:
        print(self.formatted_message(log_event).decode(self.encoding))

