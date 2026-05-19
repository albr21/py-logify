import sys
from ..filter import Filter
from ..appender import Appender
from ..layout import Layout
from ..layouts.basic import Basic
from ..level import Level

class File(Appender):
    """
    Appender that writes log events to a file.
    """

    # @param name [str] The name of the appender
    # @param file_path [str] The path to the file where log events will be written
    # @param level [Level] The minimum log level for this appender (default: Level.DEBUG)
    # @param layout [Layout] The layout to use for formatting log events (default: None, which means use the appender's layout)
    # @param encoding [str] The encoding to use for output (default: None, which means use the system default encoding)
    # @param filters [list] The list of filters to apply (default: None, which means use the appender's filters)
    # @return [None] No return value
    def __init__(self, name: str, file_path: str, *, level: Level = Level.DEBUG, layout: Layout = Basic(), encoding: str | None = None, filters: list[Filter] | None = None) -> None:
        super().__init__(name, level=level, layout=layout, encoding=encoding, filters=filters)
        self.file_path = file_path
        self.__create_log_file()

    # Write the log event
    # @param log_event [LogEvent] The log event to write
    # @return [None] No return value
    def write(self, log_event) -> None:
        try:
          with open(self.file_path, 'ab') as log_file:
              log_file.write(self.formatted_message(log_event))
        except Exception as e: # pragma: no cover
            print(f"File Appender - Failed to write log event to file {self.file_path}: {e}", file=sys.stderr)

    # Create the log file if it does not exist
    # @raises Exception if there is an error while creating the log file
    # @return [None] No return value
    def __create_log_file(self) -> None:
        try:
            with open(self.file_path, 'ab'):
                pass
        except Exception as e: # pragma: no cover
            print(f"File Appender - Failed to create log file {self.file_path}: {e}", file=sys.stderr)
