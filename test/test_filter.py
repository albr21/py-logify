from filter import Filter
from log_event import LogEvent
from level import Level

class TestFilter:
    def test_filter_default(self):
        f = Filter("filter1")
        log_event = LogEvent(logger_name="TestLogger", time="", level=Level.INFO, message="This is a test log message.")
        assert f.allow(log_event) == log_event

    def test_filter_deny(self):
        class BlockAll(Filter):
            def allow(self, log_event: LogEvent) -> LogEvent | None:
                return None

        f = BlockAll("filter2")
        assert f.allow(LogEvent(logger_name="TestLogger", time="", level=Level.INFO, message="This is a test log message.")) is None