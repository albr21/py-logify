from logger import Logger
from layouts.basic import Basic
from appenders.string_io import StringIO as StringIOAppender


class TestLoggerAppenders:
    def setup_method(self):
        self.logger = Logger("TestLogger")

    def _make_appender(self, name: str) -> StringIOAppender:
        return StringIOAppender(name, layout=Basic())

    def test_logger_appenders_add_one_appender(self):
        self.logger.add_appender(self._make_appender("Appender1"))

        assert len(self.logger.appenders) == 1
        assert self.logger.appenders[0].name == "Appender1"

    def test_logger_appenders_add_multiple_appenders(self):
        self.logger.add_appenders([
            self._make_appender("Appender1"),
            self._make_appender("Appender2"),
        ])

        assert len(self.logger.appenders) == 2
        assert self.logger.appenders[0].name == "Appender1"
        assert self.logger.appenders[1].name == "Appender2"

    def test_logger_appenders_remove_one_appender(self):
        self.logger.add_appenders([
            self._make_appender("Appender1"),
            self._make_appender("Appender2"),
        ])

        self.logger.remove_appender("Appender1")

        assert len(self.logger.appenders) == 1
        assert self.logger.appenders[0].name == "Appender2"

    def test_logger_appenders_remove_multiple_appenders(self):
        self.logger.add_appenders([
            self._make_appender("Appender1"),
            self._make_appender("Appender2"),
            self._make_appender("Appender3"),
        ])

        self.logger.remove_appenders(["Appender1", "Appender3"])

        assert len(self.logger.appenders) == 1
        assert self.logger.appenders[0].name == "Appender2"

    def test_logger_appenders_clear_appenders(self):
        self.logger.add_appenders([
            self._make_appender("Appender1"),
            self._make_appender("Appender2"),
        ])

        self.logger.clear_appenders()

        assert len(self.logger.appenders) == 0

    def test_logger_appenders_get_appender_by_name(self):
        appender1 = self._make_appender("Appender1")
        appender2 = self._make_appender("Appender2")
        self.logger.add_appenders([appender1, appender2])

        retrieved_appender = self.logger.appender("Appender1")
        assert retrieved_appender is appender1

    def test_logger_appenders_get_non_existent_appender_returns_none(self):
        self.logger.add_appender(self._make_appender("Appender1"))

        retrieved_appender = self.logger.appender("NonExistentAppender")
        assert retrieved_appender is None
