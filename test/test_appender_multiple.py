from logify.logger import Logger
from logify.level import Level
from logify.layouts.basic import Basic
from logify.appenders.file import File as FileAppender
from logify.appenders.string_io import StringIO as StringIOAppender


class TestAppenderMultiple:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def test_appender_multiple(self, tmp_path):
        # Arrange
        log_file = tmp_path / "test_log.log"
        file_appender = FileAppender("TestFileAppender", str(log_file), layout=Basic())
        string_io_appender = StringIOAppender("TestStringIOAppender", layout=Basic())
        self.logger.add_appenders([file_appender, string_io_appender])

        # Act
        self.logger.log(Level.INFO, "This is a test log message.")

        # Assert
        log_contents = log_file.read_text(encoding="utf-8")
        assert "This is a test log message." in log_contents

        string_io_contents = string_io_appender.get_value()
        assert "This is a test log message." in string_io_contents
