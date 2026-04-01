import pytest
from logify.logger import Logger
from logify.level import Level
from logify.layouts.basic import Basic
from logify.appenders.string_io import StringIO as StringIOAppender


class TestLoggerLevel:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def _make_appender(self, level: Level) -> StringIOAppender:
        return StringIOAppender("TestStringIOAppender", level=level, layout=Basic())

    def test_logger_level_all(self):
        appender = self._make_appender(Level.ALL)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" in content
        assert "Debug message" in content
        assert "Info message" in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_trace(self):
        appender = self._make_appender(Level.TRACE)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" in content
        assert "Debug message" in content
        assert "Info message" in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_debug(self):
        appender = self._make_appender(Level.DEBUG)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" in content
        assert "Info message" in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_info(self):
        appender = self._make_appender(Level.INFO)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" not in content
        assert "Info message" in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_warn(self):
        appender = self._make_appender(Level.WARN)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" not in content
        assert "Info message" not in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_error(self):
        appender = self._make_appender(Level.ERROR)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" not in content
        assert "Info message" not in content
        assert "Warn message" not in content
        assert "Error message" in content
        assert "Fatal message" in content

    def test_logger_level_fatal(self):
        appender = self._make_appender(Level.FATAL)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" not in content
        assert "Info message" not in content
        assert "Warn message" not in content
        assert "Error message" not in content
        assert "Fatal message" in content

    def test_logger_level_off(self):
        appender = self._make_appender(Level.OFF)
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" not in content
        assert "Info message" not in content
        assert "Warn message" not in content
        assert "Error message" not in content
        assert "Fatal message" not in content
        assert content == ""

    def test_logger_level_invalid(self):
        with pytest.raises(ValueError):
            StringIOAppender("TestStringIOAppender", level="invalid_level", layout=Basic()) # type: ignore

    def test_logger_level_log_methods(self):
        appender = self._make_appender(Level.DEBUG)
        self.logger.add_appender(appender)

        self.logger.trace("Trace message")
        self.logger.debug("Debug message")
        self.logger.info("Info message")
        self.logger.warn("Warn message")
        self.logger.error("Error message")
        self.logger.fatal("Fatal message")

        content = appender.get_value()
        assert "Trace message" not in content
        assert "Debug message" in content
        assert "Info message" in content
        assert "Warn message" in content
        assert "Error message" in content
        assert "Fatal message" in content