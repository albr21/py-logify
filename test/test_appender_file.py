from logger import Logger
from level import Level
from layouts.basic import Basic
from appenders.file import File as FileAppender


class TestAppenderFile:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def test_appender_file(self, tmp_path):
        log_file = tmp_path / "test_log.log"
        appender = FileAppender("TestFileAppender", str(log_file), layout=Basic())
        self.logger.add_appender(appender)

        self.logger.log(Level.INFO, "This is a test log message.")

        log_contents = log_file.read_text(encoding="utf-8")
        assert "This is a test log message." in log_contents
