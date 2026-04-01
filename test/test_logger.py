from logify.logger import Logger

class TestLogger:
    def test_logger_creation(self):
        logger = Logger("TestLogger")
        assert logger.name == "TestLogger"

    def test_logger_raises_attribute_error(self):
        logger = Logger("TestLogger")
        try:
            logger.non_existent_attribute
            assert False, "Expected AttributeError"
        except AttributeError:
            pass