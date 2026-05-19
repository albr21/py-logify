import sys
from logify.appenders.string_io import StringIO as StringIOAppender
from logify.layouts.basic import Basic
from logify.level import Level
from logify.filter import Filter
from logify.log_event import LogEvent

class TestAppender:
    def test_appender_add_filter(self):
        class AllowAll(Filter):
            def allow(self, log_event: LogEvent) -> LogEvent | None:
                return log_event

        allow_all = AllowAll(name="allow_all")
        self.appender = StringIOAppender("test", layout=Basic())
        self.appender.add_filter(allow_all)
        event = LogEvent(logger_name="logger", time="", level=Level.INFO, message="allowed")
        self.appender.append(event)
        assert "allowed" in self.appender.get_value()

    def test_appender_add_filters(self):
        class AllowAll(Filter):
            def allow(self, log_event: LogEvent) -> LogEvent | None:
                return log_event

        allow_all = AllowAll(name="allow_all")
        self.appender = StringIOAppender("test", layout=Basic())
        self.appender.add_filters([allow_all])
        event = LogEvent(logger_name="logger", time="", level=Level.INFO, message="allowed")
        self.appender.append(event)
        assert "allowed" in self.appender.get_value()

    def test_appender_remove_filter(self):
        class BlockAll(Filter):
            def allow(self, log_event: LogEvent) -> LogEvent | None:
                return None

        block_all = BlockAll(name="block_all")
        self.appender = StringIOAppender("test", layout=Basic(), filters=[block_all])
        event = LogEvent(logger_name="logger", time="", level=Level.INFO, message="blocked")
        self.appender.append(event)
        assert self.appender.get_value() == ""

        self.appender.remove_filter("block_all")
        self.appender.append(event)
        assert "blocked" in self.appender.get_value()

    def test_appender_clear_filters(self):
        class BlockAll(Filter):
            def allow(self, log_event: LogEvent) -> LogEvent | None:
                return None

        self.appender = StringIOAppender("test", layout=Basic(), filters=[BlockAll(name="block_all")])
        event = LogEvent(logger_name="logger", time="", level=Level.INFO, message="blocked")
        self.appender.append(event)
        assert self.appender.get_value() == ""

        self.appender.clear_filters()
        self.appender.append(event)
        assert "blocked" in self.appender.get_value()

    def test_appender_with_valid_encoding(self):
        appender = StringIOAppender("test", layout=Basic(), encoding="utf-8")
        assert appender.encoding == "utf-8"

    def test_appender_with_default_encoding(self):
        appender = StringIOAppender("test", layout=Basic())
        assert appender.encoding == sys.getdefaultencoding()

    def test_appender_invalid_encoding_raises(self):
        appender = StringIOAppender("test", layout=Basic(), encoding="invalid-encoding")
        assert appender.encoding == sys.getdefaultencoding()
