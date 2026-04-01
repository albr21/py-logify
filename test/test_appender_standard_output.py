from logify.logger import Logger
from logify.level import Level
from logify.layouts.basic import Basic
from logify.layouts.colorized import Colorized
from logify.appenders.standard_output import StandardOutput as StandardOutputAppender


class TestAppenderStandardOutput:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def test_appender_standard_output(self, capsys):
        appender = StandardOutputAppender("TestStandardOutputAppender", layout=Basic())
        self.logger.add_appender(appender)

        self.logger.log(Level.INFO, "This is a test log message.")

        captured = capsys.readouterr()
        assert "This is a test log message." in captured.out

    def test_appender_standard_output_with_colorized_layout(self, capsys):
        colorized_layout = Colorized()
        appender = StandardOutputAppender("TestStandardOutputAppenderWithColor", layout=colorized_layout)
        self.logger.add_appender(appender)

        self.logger.log(Level.INFO, "This is a test log message with color.")

        captured = capsys.readouterr()
        assert "This is a test log message with color." in captured.out

    def test_appender_standard_output_colorized_layout_all_log_levels(self, capsys):
        colorized_layout = Colorized()
        appender = StandardOutputAppender(
            "TestStandardOutputAppenderWithColorAllLevels",
            layout=colorized_layout,
            level=Level.TRACE,
        )
        self.logger.add_appender(appender)

        self.logger.log(Level.TRACE, "Trace message")
        self.logger.log(Level.DEBUG, "Debug message")
        self.logger.log(Level.INFO, "Info message")
        self.logger.log(Level.WARN, "Warn message")
        self.logger.log(Level.ERROR, "Error message")
        self.logger.log(Level.FATAL, "Fatal message")
