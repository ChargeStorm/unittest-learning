import pytest
from unittest import mock
import os
import requests

VARIABLE = 'original_value'

def function_to_mock():
    return 'original result'

class ClassToMock:
    def method(self):
        return 'original method result'

class TestMocking:
    """
    Mocking is a technique used in unit testing to replace real objects with mock objects.
    This is useful when you want to isolate the code being tested from external dependencies.
    """
    def test_mock_variable(self):
        """
        This test demonstrates mocking a variable.
        """
        with mock.patch('tests.test_mocking.VARIABLE', 'mocked_value'):
            assert VARIABLE == 'mocked_value'

    def test_mock_function(self):
        """
        This test demonstrates mocking a function.
        """
        def mock_function():
            return 'mocked result'
        with mock.patch('tests.test_mocking.function_to_mock', mock_function):
            assert function_to_mock() == 'mocked result'

    def test_mock_class(self):
        """
        This test demonstrates mocking a class.
        """
        class MockClass:
            def method(self):
                return 'mocked method result'
        with mock.patch('tests.test_mocking.ClassToMock', MockClass):
            instance = ClassToMock()
            assert instance.method() == 'mocked method result'

    def test_mock_file_input(self):
        """
        This test demonstrates mocking file input.
        """
        mock_open = mock.mock_open(read_data='mocked file content')
        with mock.patch('builtins.open', mock_open):
            with open('dummy_file.txt') as f:
                assert f.read() == 'mocked file content'

    def test_mock_directory_structure(self):
        """
        This test demonstrates mocking directory structure.
        """
        with mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt']):
            assert os.listdir('dummy_directory') == ['file1.txt', 'file2.txt']

    def test_mock_api_response(self):
        """
        This test demonstrates mocking an API response.
        """
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        with mock.patch('requests.get', return_value=mock_response):
            response = requests.get('https://api.example.com/data')
            assert response.status_code == 200
            assert response.json() == {'key': 'value'}
