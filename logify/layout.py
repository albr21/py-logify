from abc import ABC, abstractmethod
from logify.log_event import LogEvent

class Layout(ABC):
    """
    Abstract base class for layouts.
    """

    # The format method should be implemented by subclasses to define how log events are formatted.
    # @param log_event [LogEvent] The log event to format
    # @return [str] The formatted log message
    @abstractmethod
    def format(self, log_event: LogEvent) -> str: # pragma: no cover
        pass
