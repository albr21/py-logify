from logger import Logger
from level import Level
from layouts.basic import Basic
from appenders.string_io import StringIO as StringIOAppender


class TestAppenderStringIO:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def test_appender_string_io(self):
        appender = StringIOAppender("TestStringIOAppender", layout=Basic())
        self.logger.add_appender(appender)

        self.logger.log(Level.INFO, "This is a test log message.")

        assert "This is a test log message." in appender.get_value()
        appender.clear()
        assert appender.get_value() == ""
