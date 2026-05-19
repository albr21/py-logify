from ..layout import Layout
from ..log_event import LogEvent
from ..level import Level

class Colorized(Layout):
    """
    Colorized layout class for formatting log events with colors
    https://www.nordtheme.com/docs/colors-and-palettes
    """

    NORD_THEME = {
        "nord_0": "\033[38;2;46;52;64m",   # Polar Night
        "nord_1": "\033[38;2;59;66;82m",   # Polar Night
        "nord_2": "\033[38;2;67;76;94m",   # Polar Night
        "nord_3": "\033[38;2;76;86;106m",  # Polar Night
        "nord_4": "\033[38;2;216;222;233m",  # Snow Storm
        "nord_5": "\033[38;2;229;233;240m",  # Snow Storm
        "nord_6": "\033[38;2;236;239;244m",  # Snow Storm
        "nord_7": "\033[38;2;143;188;187m",  # Frost
        "nord_8": "\033[38;2;136;192;208m",  # Frost
        "nord_9": "\033[38;2;129;161;193m",  # Frost
        "nord_10": "\033[38;2;94;129;172m",  # Frost
        "nord_11": "\033[38;2;191;97;106m",  # Aurora
        "nord_12": "\033[38;2;208;135;112m",  # Aurora
        "nord_13": "\033[38;2;235;203;139m",  # Aurora
        "nord_14": "\033[38;2;163;190;140m",  # Aurora
        "nord_15": "\033[38;2;180;142;173m"   # Aurora
    }

    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

    # Format the log event into a string
    # @param log_event [LogEvent] The log event to format
    # @return [str] The formatted log message
    def format(self, log_event: LogEvent) -> str:
        return f"{log_event.time} [{self.__apply_color(str(log_event.level).ljust(5), log_event.level)}] -- {log_event.logger_name}: {log_event.message}\n"

    # Apply the appropriate color to the text based on the log level
    # @param text [str] The text to colorize
    # @param level [Level] The log level to determine the color
    # @return [str] The colorized text
    def __apply_color(self, text: str, level: Level) -> str:
        color = self.__color_for_level(level)
        return f"{color}{text}{self.RESET}"
        # Alternative hex codes:

    # Determine the color to use based on the log level
    # @param level [Level] The log level to determine the color
    # @return [str] The ANSI escape code for the color corresponding to the log level
    def __color_for_level(self, level: Level) -> str:
        match level:
            case Level.TRACE:
                return self.NORD_THEME["nord_8"]
            case Level.DEBUG:
                return self.BOLD + self.NORD_THEME["nord_9"]
            case Level.INFO:
                return self.BOLD + self.NORD_THEME["nord_14"]
            case Level.WARN:
                return self.BOLD + self.NORD_THEME["nord_13"]
            case Level.ERROR:
                return self.BOLD + self.NORD_THEME["nord_11"]
            case Level.FATAL:
                return self.BOLD + self.NORD_THEME["nord_12"]
            case _: # pragma: no cover
                return self.NORD_THEME["nord_4"]
