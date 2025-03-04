import pytest


class CustomException(Exception):
    """A custom exception for demonstration purposes."""

    pass


def function_that_raises(value):
    """
    A function for demonstrating exception handling in tests.

    This function raises a ValueError if the input is negative, a KeyError if the input is 0, and a CustomException if the input is 99.
    """
    if value < 0:
        raise ValueError("Negative value not allowed")
    elif value == 0:
        raise KeyError("Value cannot be zero")
    elif value == 99:
        raise CustomException("99 is a special case")
    else:
        return value


class TestExceptionHandling:
    """
    This class demonstrates various ways to handle and test exceptions using pytest.
    """

    def test_value_error(self):
        """
        This test verifies that a ValueError is raised for negative input.
        """
        with pytest.raises(ValueError, match="Negative value not allowed"):
            function_that_raises(-1)

    def test_key_error(self):
        """
        This test verifies that a KeyError is raised for zero input.
        """
        with pytest.raises(KeyError, match="Value cannot be zero"):
            function_that_raises(0)

    def test_custom_exception(self):
        """
        This test verifies that a CustomException is raised for input 99.
        """
        with pytest.raises(CustomException, match="99 is a special case"):
            function_that_raises(99)

    @pytest.mark.parametrize(
        "input_value, expected_exception, expected_message",
        [
            (-1, ValueError, "Negative value not allowed"),
            (0, KeyError, "Value cannot be zero"),
            (99, CustomException, "99 is a special case"),
        ],
    )
    def test_multiple_exceptions(
        self, input_value, expected_exception, expected_message
    ):
        """
        This test verifies multiple exception scenarios using parameterized inputs.
        """
        with pytest.raises(expected_exception, match=expected_message):
            function_that_raises(input_value)

    def test_no_exception(self):
        """
        This test verifies that no exception is raised for positive input except 99.
        """
        assert function_that_raises(1) == 1
        assert function_that_raises(50) == 50

    def test_inspecting_exception(self):
        """
        This test inspects the attributes of a raised exception.
        """
        with pytest.raises(ValueError) as excinfo:
            function_that_raises(-1)
        assert excinfo.type is ValueError
        assert excinfo.value.args[0] == "Negative value not allowed"
