from logify.appender import Appender
from logify.filter import Filter
from logify.layout import Layout
from logify.layouts.basic import Basic
from logify.level import Level
from io import BytesIO

class StringIO(Appender):
    """
    Appender that writes log events to a string buffer (in-memory).
    """

    # @param name [str] The name of the appender
    # @param level [Level] The minimum log level for this appender (default: Level.DEBUG)
    # @param layout [Layout] The layout to use for formatting log events (default: None, which means use the appender's layout)
    # @param encoding [str] The encoding to use for output (default: None, which means use the system default encoding)
    # @param filters [list] The list of filters to apply (default: None, which means use the appender's filters)
    # @return [None] No return value
    def __init__(self, name: str, *, level: Level = Level.DEBUG, layout: Layout = Basic(), encoding: str | None = None, filters: list[Filter] | None = None) -> None:
        super().__init__(name, level=level, layout=layout, encoding=encoding, filters=filters)
        self.buffer = BytesIO()

    # Write the log event
    # @param log_event [LogEvent] The log event to write
    # @return [None] No return value
    def write(self, log_event) -> None:
        self.buffer.write(self.formatted_message(log_event))


    # Get the current value of the string buffer
    # @return [str] The current contents of the string buffer
    def get_value(self) -> str:
        return self.buffer.getvalue().decode(self.encoding)
    
    # Clear the string buffer
    # @return [None] No return value
    def clear(self) -> None:
        self.buffer.seek(0)
        self.buffer.truncate(0)
