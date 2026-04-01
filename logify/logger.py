from logify.appender import Appender
from logify.log_event import LogEvent
from logify.level import Level

class Logger():
    """
    Logger class for logify messages with different levels and appenders.
    """

    # @param name [str] The name of the logger
    # @param appenders [list[Appender]] A list of appenders to which log events will be sent. Defaults to an empty list.
    # @return [None] No return value
    def __init__(self, name: str, *, appenders: list[Appender] = []) -> None:
        self.name = name
        self.appenders = appenders.copy()

    # Auto-generate log methods for each log level (trace, debug, info, warn, error, fatal)
    def __getattr__(self, name):
        if name in ['trace', 'debug', 'info', 'warn', 'error', 'fatal']:
            level = getattr(Level, name.upper())
            def log_method(message: str | None = None, *, exception: Exception | None = None, data: dict | None = None, callback=None, **kwargs) -> None:
                self.log(level, message, exception=exception, data=data, callback=callback, **kwargs)
            return log_method
        raise AttributeError(f"'Logger' object has no attribute '{name}'")

    # Generic log method
    # @param level [Level] The log level
    # @param message [str] The log message
    # @param exception [Exception, nil] An optional exception associated with the log event
    # @param data [dict, nil] An optional dictionary of additional data to include with the log event
    # @param callback [callable, nil] An optional callback to be invoked after the log event is processed
    # @param kwargs [dict] Additional keyword arguments
    # @return [None] No return value
    def log(self, level: Level, message: str | None = None, *, exception: Exception | None = None, data: dict | None = None, callback=None, **kwargs) -> None:
        log_event = LogEvent(
            logger_name=self.name,
            level=level,
            message=message,
            time=kwargs.get('time'),
            exception=exception,
            data=data
        )
        self.__append(log_event)


    # Enable to get an appender by name
    # @param appender [str] The name of the appender to retrieve
    # @return [Appender | None] The appender with the specified name
    #                           None if no such appender exists
    def appender(self, appender: str) -> Appender | None:
        for a in self.appenders:
            if a.name == appender:
                return a
        return None
    
    # Add an appender to the logger
    # @param appender [Appender] The appender to add
    #                            Appender must not be None, must not already be added,
    #                            must not have a name conflict with an existing appender
    # @raises ValueError if appender is None, already added, or has a name conflict
    # @return [None] No return value
    def add_appender(self, appender: Appender) -> None:
        if appender in self.appenders: raise ValueError(f"Logger - Appender with name '{appender.name}' already exists in logger {self.name}")
        if isinstance(appender, Appender) is False: raise ValueError("Logger - Appender must be an instance of Appender")
        self.appenders.append(appender)

    # Add multiple appenders to the logger
    # @param appenders [list[Appender]] The list of appenders to add
    #                                  Each appender must not be None, must not already be added,
    #                                  must not have a name conflict with an existing appender
    # @raises ValueError if any appender is None, already added, or has a name conflict
    # @return [None] No return value
    def add_appenders(self, appenders: list[Appender]) -> None:
        for appender in appenders:
            self.add_appender(appender)

    # Remove an appender from the logger by name
    # @param appender [str] The name of the appender to remove
    # @return [None] No return value
    def remove_appender(self, appender: str) -> None:
        self.appenders = [a for a in self.appenders if a.name != appender]

    # Remove multiple appenders from the logger by name
    # @param appenders [list[str]] The list of names of the appenders to remove
    # @return [None] No return value
    def remove_appenders(self, appenders: list[str]) -> None:
        for appender in appenders:
            self.remove_appender(appender)

    # Clear all appenders from the logger
    # @return [None] No return value
    def clear_appenders(self) -> None:
        self.appenders.clear()

    # Append a log event to all appenders of this logger
    # @param log_event [LogEvent] The log event to append
    # @return [None] No return value
    def __append(self, log_event: LogEvent) -> None:
        for appender in self.appenders:
            appender.append(log_event)

    
