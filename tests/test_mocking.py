from unittest import mock
from tempfile import TemporaryDirectory
import os
import requests

VARIABLE = "original_value"

def function_to_mock(arg1: str = "original result"):
    return arg1

class ClassToMock:
    variable = "original variable"
    def method(self):
        return "original method result"

class TestMockingVariables:
    """
    Mocking is a technique used in unit testing to replace real objects with mock objects.
    This is useful when you want to isolate the code being tested from external dependencies.
    """
    def test_mock_variable_unittest(self):
        """
        This test demonstrates mocking a variable with Pythons
        built-in unittest.mock library.
        """
        with mock.patch("tests.test_mocking.VARIABLE", "mocked_value"):
            assert VARIABLE == "mocked_value"

    def test_mock_variable_pytest(self, mocker):
        """
        This test demonstrates mocking a variable using the pytest-mock library.
        """
        mocker.patch("tests.test_mocking.VARIABLE", "mocked_value")
        assert VARIABLE == "mocked_value"


class TestMockingFunctions:
    """
    This class demonstrates how to mock functions.
    """

    def test_mock_function_unittest(self):
        """
        This test demonstrates mocking a function with Pythons
        built-in unittest.mock library.
        """
        def mock_function():
            return "mocked result"
        with mock.patch("tests.test_mocking.function_to_mock", mock_function):
            assert function_to_mock() == "mocked result"

    def test_mock_function_unittest_assert_called_with(self):
        """
        This test demonstrates how to assert that a mocked function
        was called with specific arguments.

        Note that we do not use a separate function here. Because then we would have
        replaced the mocked function with our function, which do not have the
        assert_called_with method.
        """

        with mock.patch("tests.test_mocking.function_to_mock") as mocked_function:
            function_to_mock("mocked result")
            mocked_function.assert_called_with("mocked result")

    def test_mock_function_pytest(self, mocker):
        """
        This test demonstrates mocking a function using the pytest-mock library.

        Note that this do not use a context manager like the unittest.mock library.
        """
        mocker.patch("tests.test_mocking.function_to_mock", return_value="mocked result")
        assert function_to_mock() == "mocked result"

    def test_mock_function_pytest_assert_called_with(self, mocker):
        """
        This test demonstrates how to assert that a mocked function
        was called with specific arguments using the pytest-mock library.

        Note that this do not use a context manager like the unittest.mock library.
        """
        mocked_function = mocker.patch("tests.test_mocking.function_to_mock")
        function_to_mock("mocked result")
        mocked_function.assert_called_with("mocked result")


class TestMockingClasses:
    """
    This class demonstrates how to mock classes, methods, and class variables.
    """
    def test_mock_class_variable_unittest(self):
        """
        This test demonstrates mocking a class variable using the
        unittest.mock library.
        """
        class MockClass:
            variable = "mocked variable"
        with mock.patch("tests.test_mocking.ClassToMock", MockClass):
            instance = ClassToMock()
            assert instance.variable == "mocked variable"

    def test_mock_class_variable_pytest(self, mocker):
        """
        This test demonstrates mocking a class variable using the pytest-mock library.
        """
        mocker.patch("tests.test_mocking.ClassToMock.variable", "mocked variable")
        instance = ClassToMock()
        assert instance.variable == "mocked variable"

    def test_mock_class_method_unittest(self):
        """
        This test demonstrates mocking a class method using the
        unittest.mock library.
        """
        class MockClass:
            def method(self):
                return "mocked method result"
        with mock.patch("tests.test_mocking.ClassToMock", MockClass):
            instance = ClassToMock()
            assert instance.method() == "mocked method result"

    def test_mock_class_method_pytest(self, mocker):
        """
        This test demonstrates mocking a class method using the pytest-mock library.
        """
        mocker.patch("tests.test_mocking.ClassToMock.method", return_value="mocked method result")
        instance = ClassToMock()
        assert instance.method() == "mocked method result"


class TestMockingFilesAndDirectories:
    def test_mock_file_unittest(self):
        """
        This test demonstrates mocking file input using the unittest.mock library.
        """
        mock_open = mock.mock_open(read_data="mocked file content")
        with mock.patch("builtins.open", mock_open):
            with open("dummy_file.txt") as f:
                assert f.read() == "mocked file content"

    def test_mock_file_pytest(self, mocker):
        """
        This test demonstrates mocking file input using the pytest-mock library.
        """
        mock_open = mocker.mock_open(read_data="mocked file content")
        mocker.patch("builtins.open", mock_open)

        with open("dummy_file.txt") as f:
            assert f.read() == "mocked file content"

    def test_mock_directory_unittest(self):
        """
        This test demonstrates mocking directory structure with files
        using the unittest.mock library.
        """
        with TemporaryDirectory() as d:
            with mock.patch("os.listdir", return_value=["file1.txt", "file2.txt"]):
                assert sorted(os.listdir(d)) == ["file1.txt",
                                                 "file2.txt"]

    def test_mock_directory_pytest(self, tmp_path):
        """
        This test demonstrates mocking directory structure with files
        using the tmp_path fixture from pytest.
        """
        d = tmp_path / "dummy_directory"
        d.mkdir()
        (d / "file1.txt").write_text("content1")
        (d / "file2.txt").write_text("content2")
        with mock.patch("os.listdir", return_value=sorted([p.name for p in d.iterdir()])):
            assert sorted(os.listdir(d)) == ["file1.txt", "file2.txt"]

class TestMockingEnvironmentVariables:
    """
    This class demonstrates how to mock environment variables.
    """
    def test_mock_environment_variable_unittest(self):
        """
        This test demonstrates mocking an environment variable using the
        unittest.mock library.
        """
        with mock.patch.dict(os.environ, {"ENV_VAR": "mocked_value"}):
            assert os.environ["ENV_VAR"] == "mocked_value"

    def test_mock_environment_variable_pytest(self, mocker):
        """
        This test demonstrates mocking an environment variable using the pytest-mock library.
        """
        mocker.patch.dict(os.environ, {"ENV_VAR": "mocked_value"})
        assert os.environ["ENV_VAR"] == "mocked_value"

class TestMockingApi:
    """
    This class demonstrates how to mock API responses.
    """
    def test_mock_api_response_unittest(self):
        """
        This test demonstrates mocking an API response.
        """
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        with mock.patch("requests.get", return_value=mock_response):
            response = requests.get("https://api.example.com/data")
            assert response.status_code == 200
            assert response.json() == {"key": "value"}

    def test_mock_api_response_pytest(self, mocker):
        """
        This test demonstrates mocking an API response using the pytest-mock library.
        """
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mocker.patch("requests.get", return_value=mock_response)
        response = requests.get("https://api.example.com/data")
        assert response.status_code == 200
        assert response.json() == {"key": "value"}

