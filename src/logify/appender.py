import sys
from abc import ABC, abstractmethod
from .layouts.basic import Basic
from .layout import Layout
from .level import Level
from .log_event import LogEvent
from .filter import Filter

class Appender(ABC):
    """
    Abstract base class for appenders.
    Appenders are responsible for taking log events and outputting them to a specific destination (e.g., console, file, network).
    """

    # @param name [str] The name of the appender
    # @param level [Level] The minimum log level for this appender (default: Level.DEBUG)
    # @param layout [Layout] The layout to use for formatting log events (default: None, which means use the appender's layout)
    # @param encoding [str] The encoding to use for output (default: None, which means use the system default encoding)
    # @param filters [list] The list of filters to apply (default: None, which means use the appender's filters)
    # @return [None] No return value
    def __init__(self, name: str, *, level: Level = Level.DEBUG, layout: Layout = Basic(), encoding: str | None = None, filters: list[Filter] | None = None) -> None:
        self.name = name
        if not isinstance(level, Level):
            raise ValueError(f"Invalid level: '{level}', must be a Level instance")
        self.level = level
        self.layout = layout
        self.__setup_encoding(encoding)
        self.filters = filters if filters is not None else []

    # Append the log event if it passes the filters and level check
    # @param log_event [LogEvent] The log event to evaluate against the filters
    # @raises Exception if there is an error while writing the log event
    # @return [None] No return value
    def append(self, log_event) -> None:
        log_event = self.__allow(log_event)
        try:
            if log_event is not None:
                self.write(log_event)
        except Exception as e: # pragma: no cover
            print(f"Appender - Failed to write log event in appender {self.name}: {e}", file=sys.stderr)     

    # Format the log event using the appender's layout and encoding
    # @param log_event [LogEvent] The log event to format
    # @return [bytes] The formatted log message as bytes
    def formatted_message(self, log_event) -> bytes:
        return self.layout.format(log_event).encode(self.encoding)

    # Abstract method to write the log event to the destination, must be implemented by subclasses
    # @param log_event [LogEvent] The log event to write
    # @raises NotImplementedError if the method is not implemented by a subclass
    # @return [None] No return value
    @abstractmethod
    def write(self, log_event) -> None: # pragma: no cover
        pass

    # Add a filter to the appender
    # @param filter [Filter] The filter to add
    #                        Filter must not be None, must not already be added,
    #                        must not have a name conflict with an existing filter
    # @raises ValueError if filter is None, already added, or has a name conflict
    # @return [None] No return value
    def add_filter(self, filter: Filter) -> None:
        if filter is None: raise ValueError("Appender - Filter must not be None")
        if filter in self.filters: raise ValueError("Appender - Filter already added")
        if any(f.name == filter.name for f in self.filters): raise ValueError(f"Appender - Filter '{filter.name}' conflict with existing filter")
        self.filters.append(filter)

    # Add multiple filters to the appender
    # @param filters [list] The list of filters to add
    #                       Each filter must not be None, must not already be added,
    #                       must not have a name conflict with an existing filter
    # @raises ValueError if any filter is None, already added, or has a name conflict
    # @return [None] No return value
    def add_filters(self, filters: list[Filter]) -> None:
        for filter in filters:
            self.add_filter(filter)

    # Remove a filter from the appender by name
    # @param filter [str] The name of the filter to remove
    # @return [None] No return value
    def remove_filter(self, filter: str) -> None:
        self.filters = [f for f in self.filters if f.name != filter]

    # Clear all filters from the appender
    # @return [None] No return value
    def clear_filters(self) -> None:
        self.filters.clear()

    # Setup the encoding for this appender
    # @param encoding [str] The encoding to use for output
    #                       If None or empty, the system default encoding will be used
    # @return [None] No return value
    def __setup_encoding(self, encoding) -> None:
        if encoding is None or encoding == '':
            self.encoding = sys.getdefaultencoding()
        else:
            try:
                ''.encode(encoding)
                self.encoding = encoding
            except LookupError:
                self.encoding = sys.getdefaultencoding()
                print(f"Appender - Invalid encoding '{encoding}' specified for appender {self.name}, using system default encoding instead #{self.encoding}", file=sys.stderr)     

    # Apply filters to determine if the log event should be allowed
    # @param log_event [LogEvent] The log event to evaluate
    # @return [LogEvent | None] The log event if allowed, or nil if denied
    def __allow(self, log_event) -> LogEvent | None:
        if Level.is_enabled(self.level, log_event.level) is False: return None

        if self.filters is not None:
            for filter in self.filters:
                log_event = filter.allow(log_event)
                if log_event is None: return None
        return log_event
