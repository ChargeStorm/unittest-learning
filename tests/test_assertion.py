import pytest


class TestAssertion:
    """
    Assertion is one of the fundamental concepts in testing, used to
    validate the expected result of a test.
    It is used to compare the actual result with the expected result.
    If the actual result matches the expected result, the test case passes;
    otherwise, it fails.
    """

    def test_assertion_pass(self):
        """
        In this test case, the assertion is True, so the test case passes.
        """
        assert 1 == 1

    @pytest.mark.xfail(reason="This test is expected to fail as a demonstration.")
    def test_assertion_fail(self):
        """
        In this test case, the assertion is False, so the test case fails.
        The 'xfail' marker indicates that this test is expected to fail.
        """
        assert 1 == 2

    @pytest.mark.xfail(reason="This test is expected to fail as a demonstration.")
    def test_assertion_with_message(self):
        """
        You can also provide a message to the assertion to make it more informative.
        Note: The message is displayed only when the assertion fails.
        """
        assert 1 == 2, "1 is not equal to 2"

    def test_list_equality(self):
        """
        This test checks if two lists are equal.
        """
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        assert list1 == list2, "The two lists should be equal"

    def test_string_contains(self):
        """
        This test checks if a string contains a substring.
        """
        string = "Hello, world!"
        substring = "world"
        assert substring in string, (
            f"The string should contain the substring '{substring}'"
        )

    def test_dict_key_presence(self):
        """
        This test checks if a key is present in a dictionary.
        """
        my_dict = {"key1": "value1", "key2": "value2"}
        assert "key1" in my_dict, "The key 'key1' should be present in the dictionary"

    def test_none_check(self):
        """
        This test checks if a variable is None.
        """
        var = None
        assert var is None, "The variable should be None"

    def test_boolean_expression(self):
        """
        This test checks the truthiness of a boolean expression.
        """
        condition = 1 + 1 == 2
        assert condition, "The boolean expression should be True"

    def test_approximate_equality(self):
        """
        This test checks if two floating-point numbers are approximately equal.
        """
        num1 = 0.1 + 0.2
        num2 = 0.3
        assert num1 == pytest.approx(num2), (
            "The two numbers should be approximately equal"
        )
