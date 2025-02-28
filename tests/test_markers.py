import pytest

class TestMarkers:
    """
    This class demonstrates the usage of various markers in pytest.

    Custom Markers:
    Custom markers allow you to categorize tests for different purposes.

    To define custom markers, you should register them in a pyproject.toml file.
    Create a pyproject.toml file in your project root with the following content:

    [tool.pytest.ini_options]
    markers = [
        "slow: marks tests as slow (deselect with '-m \"not slow\"')",
        "fast: marks tests as fast",
        "regression: marks tests for regression testing"
    ]

    Usage:
    - Run tests marked as slow:
      pytest -m slow
    - Run tests excluding the slow ones:
      pytest -m "not slow"
    - Run tests marked for regression:
      pytest -m regression
    """

    @pytest.mark.skip(reason="Skipping this test for demonstration purposes")
    def test_skip_example(self):
        """
        This test is skipped and will not be run.
        """
        assert 1 == 1

    @pytest.mark.skipif(True, reason="This test is conditionally skipped")
    def test_conditional_skip(self):
        """
        This test is conditionally skipped based on some condition.
        """
        assert True

    @pytest.mark.xfail(reason="This test is expected to fail")
    def test_expected_fail(self):
        """
        This test is expected to fail.
        """
        assert 1 == 2

    @pytest.mark.parametrize("input_data, expected", [
        (1, 2),
        (2, 3),
        (3, 4),
    ])
    def test_parametrized(self, input_data, expected):
        """
        This test uses the parametrize marker to test multiple inputs.

        You can read more about parametrized tests in the
        [parametrization](parametrization.md#TestParametrization) section.
        """
        assert input_data + 1 == expected