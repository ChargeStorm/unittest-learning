import pytest

class TestParametrization:
    """
    This class demonstrates the usage of parameterized tests in pytest.
    Parameterized tests allow you to define multiple sets of arguments
    for a single test function.
    """

    @pytest.mark.parametrize("input_data, expected", [
        (1, 2),
        (2, 3),
        (3, 4),
    ])
    def test_add_one(self, input_data, expected):
        """
        This test checks if adding 1 to the input_data produces the expected result.
        """
        assert input_data + 1 == expected

    @pytest.mark.parametrize("string, substring, expected", [
        ("Hello, world!", "world", True),
        ("Hello, world!", "Python", False),
        ("Pytest is great", "great", True),
    ])
    def test_string_contains(self, string, substring, expected):
        """
        This test checks if a substring is present in the main string.
        """
        assert (substring in string) == expected

    @pytest.mark.parametrize("list1, list2, expected", [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [2, 1], False),
        ([], [], True),
    ])
    def test_list_equality(self, list1, list2, expected):
        """
        This test checks if two lists are equal.
        """
        assert (list1 == list2) == expected

    @pytest.mark.parametrize("dividend, divisor, expected", [
        (10, 2, 5),
        (9, 3, 3),
        (5, 2, 2.5),
    ])
    def test_division(self, dividend, divisor, expected):
        """
        This test checks if division produces the expected result.
        """
        assert dividend / divisor == expected

    @pytest.mark.parametrize("base, exponent, expected", [
        (2, 3, 8),
        (3, 2, 9),
        (5, 0, 1),
    ])
    def test_power(self, base, exponent, expected):
        """
        This test checks if raising a base to an exponent gives the expected result.
        """
        assert base ** exponent == expected

    @pytest.mark.parametrize("person, request_param, expected_value", [
        ({"name": "Alice", "age": 30}, "name", "Alice"),
        ({"name": "Bob", "age": 25}, "age", 25),
        ({"name": "Charlie", "age": 35}, "name", "Charlie"),
    ])
    def test_dict_values(self, person, request_param, expected_value):
        """
        This test checks if the dictionary returns the expected value for a given key.
        """
        assert person[request_param] == expected_value

    @pytest.mark.parametrize("integer_list, target_sum, expected", [
        ([1, 2, 3], 6, True),
        ([1, 2, 3], 7, False),
        ([1, 1, 1], 3, True),
    ])
    def test_sum_of_list(self, integer_list, target_sum, expected):
        """
        This test checks if the sum of the list equals the target sum.
        """
        assert (sum(integer_list) == target_sum) == expected