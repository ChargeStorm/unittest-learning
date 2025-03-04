import logging
import pytest

# Configure the root logger or a specific logger for the test
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@pytest.fixture(scope="function")
def log_start_and_end(request):
    """
    Fixture for demonstration purposes of TestLoggingDuringTests.

    Fixture to log the start and end of each test.
    """
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Finished test: {request.node.name}")


class TestLoggingDuringTests:
    """
    Class to demonstrate logging within multiple tests in a class.
    """

    def test_addition(self):
        """
        Test to demonstrate logging within tests. This test checks the addition operation.
        """
        logger.info("Starting test_addition")
        a = 2
        b = 3
        logger.debug(f"Values: a={a}, b={b}")
        result = a + b
        logger.debug(f"Result: {result}")
        logger.info("Asserting the result")
        assert result == 5
        logger.info("Finished test_addition")

    def test_subtraction(self):
        """
        Test to demonstrate logging within tests. This test checks the subtraction operation.
        """
        logger.info("Starting test_subtraction")
        a = 10
        b = 5
        logger.debug(f"Values: a={a}, b={b}")
        result = a - b
        logger.debug(f"Result: {result}")
        logger.info("Asserting the result")
        assert result == 5
        logger.info("Finished test_subtraction")

    def test_multiplication(self):
        """
        Test to check the multiplication operation.
        """
        logger.info("Starting test_multiplication")
        a = 3
        b = 4
        logger.debug(f"Values: a={a}, b={b}")
        result = a * b
        logger.debug(f"Result: {result}")
        logger.info("Asserting the result")
        assert result == 12
        logger.info("Finished test_multiplication")

    def test_division(self):
        """
        Test to check the division operation and handle division by zero.
        """
        logger.info("Starting test_division")
        a = 8
        b = 2
        logger.debug(f"Values: a={a}, b={b}")
        try:
            result = a / b
            logger.debug(f"Result: {result}")
            logger.info("Asserting the result")
            assert result == 4
        except ZeroDivisionError as e:
            logger.error("Caught division by zero exception", exc_info=True)
            pytest.fail("Division by zero")
        logger.info("Finished test_division")

    def test_division_by_zero(self):
        """
        Test to check division by zero operation.
        """
        logger.info("Starting test_division_by_zero")
        a = 8
        b = 0
        logger.debug(f"Values: a={a}, b={b}")
        with pytest.raises(ZeroDivisionError):
            result = a / b
        logger.info("Finished test_division_by_zero")


def function_to_log():
    """
    Function for demonstration purposes of TestLoggingCapture.

    This function logs messages at different severity levels.
    """
    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")


def custom_log_function():
    """
    Function for demonstration purposes of TestLoggingCapture.

    This function logs a custom message.
    """
    logger.info("This is a custom log message")


def check_log_contains(caplog, level, message):
    """
    Function for demonstration purposes of TestLoggingCapture.

    Helper function to assert that a specific log message at a given level is captured.
    """
    assert any(
        record.levelno == level and message in record.message
        for record in caplog.records
    )


class TestLoggingCapture:
    """
    This class demonstrates how to capture and test logging output using pytest.
    """

    def test_capture_log_output(self, caplog):
        """
        This test captures log output and verifies it contains the expected messages.
        """
        with caplog.at_level(logging.DEBUG):
            function_to_log()

        # Caplog records the log messages and their levels
        assert "Debug message" in caplog.text
        assert "Information message" in caplog.text
        assert "Warning message" in caplog.text
        assert "Error message" in caplog.text
        assert "Critical message" in caplog.text

        # Optional: Verify the log level for each message
        assert any(record.levelno == logging.DEBUG for record in caplog.records)
        assert any(record.levelno == logging.INFO for record in caplog.records)
        assert any(record.levelno == logging.WARNING for record in caplog.records)
        assert any(record.levelno == logging.ERROR for record in caplog.records)
        assert any(record.levelno == logging.CRITICAL for record in caplog.records)

    def test_custom_log_message(self, caplog):
        """
        This test captures a custom log message and verifies its content.
        """
        with caplog.at_level(logging.INFO):
            custom_log_function()

        assert "This is a custom log message" in caplog.text

        # Optionally, check that the message is logged at the expected level
        assert any(record.levelno == logging.INFO for record in caplog.records)

    def test_no_logs_at_lower_level(self, caplog):
        """
        This test ensures no logs are captured below a specific level.
        """
        with caplog.at_level(logging.WARNING):
            custom_log_function()

        # Since the logging level is set to WARNING, the INFO log should not appear
        assert "This is a custom log message" not in caplog.text

    def test_clear_logs(self, caplog):
        """
        This test demonstrates how to clear captured logs between tests or check points.
        """
        with caplog.at_level(logging.INFO):
            custom_log_function()

        assert "This is a custom log message" in caplog.text

        # Clear the captured logs
        caplog.clear()

        assert "This is a custom log message" not in caplog.text

    def test_assert_log_contains(self, caplog):
        """
        This test demonstrates a helper function to assert that a specific log message is captured.
        """
        with caplog.at_level(logging.INFO):
            custom_log_function()

        check_log_contains(caplog, logging.INFO, "This is a custom log message")
