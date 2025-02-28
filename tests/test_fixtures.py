import pytest

class TestFixtures:
    """
    Fixtures in Pytest provide a way to initialize resources and to provide
    these resources to the test functions.

    It's a great way to define reusable data or setup code that can be used
    across multiple tests.

    !!! Note
        Fixtures usually does not go into a class, but for demonstration
        purposes, we are using a class here to group the fixtures together.
    """

    @pytest.fixture
    def simple_data(self):
        """
        This fixture provides a simple dataset for testing purposes.
        """
        return {"key": "value", "number": 42}

    @pytest.fixture
    def complex_data(self):
        """
        This fixture provides a more complex dataset.
        """
        data = {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"},
            ],
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        }
        return data

    @pytest.fixture(scope='module')
    def database_connection(self):
        """
        This fixture mocks a database connection. It is set to module
        scope so it will be setup once per module and shared between tests.
        """
        connection = "database_connection"
        yield connection
        # Tear down
        connection = None
        print("Closed database connection")

    @pytest.fixture(scope='session')
    def app_config(self):
        """
        This fixture provides application configuration.
        It is set to session scope so it will be setup once per test session.
        """
        config = {
            "version": "1.0.0",
            "name": "Sample Application"
        }
        yield config
        # No explicit teardown required for this example

    @pytest.fixture
    def temp_file(self, tmp_path):
        """
        This fixture creates a temporary file for testing.
        """
        file = tmp_path / "temp_file.txt"
        file.write_text("Temporary file content")
        return file

    @pytest.fixture
    def mock_environment_variable(self, monkeypatch):
        """
        This fixture mocks an environment variable using the monkeypatch plugin from pytest.
        """
        monkeypatch.setenv("ENV_VAR", "mocked_value")
        yield
        monkeypatch.undo()

class TestUsingFixtures(TestFixtures):
    """
    This class demonstrates the usage of the fixtures
    defined in the TestFixtures class.
    """

    def test_simple_data_fixture(self, simple_data):
        """
        This test uses the simple_data fixture.
        """
        assert simple_data["key"] == "value"
        assert simple_data["number"] == 42

    def test_complex_data_fixture(self, complex_data):
        """
        This test uses the complex_data fixture.
        """
        users = complex_data["users"]
        assert isinstance(users, list)
        assert len(users) == 2
        assert users[0]["name"] == "Alice"
        assert complex_data["settings"]["theme"] == "dark"

    def test_database_connection_fixture(self, database_connection):
        """
        This test uses the database_connection fixture.
        """
        assert database_connection == "database_connection"

    def test_app_config_fixture(self, app_config):
        """
        This test uses the app_config fixture.
        """
        assert app_config["version"] == "1.0.0"
        assert app_config["name"] == "Sample Application"

    def test_temp_file_fixture(self, temp_file):
        """
        This test uses the temp_file fixture.
        """
        assert temp_file.read_text() == "Temporary file content"

    def test_mock_environment_variable_fixture(self, mock_environment_variable):
        """
        This test uses the mock_environment_variable fixture.
        """
        import os
        assert os.getenv("ENV_VAR") == "mocked_value"

    def test_combined_fixtures(self, simple_data, complex_data, app_config):
        """
        This test uses multiple fixtures to verify combined use.
        """
        assert simple_data["key"] == "value"
        assert len(complex_data["users"]) == 2
        assert app_config["version"] == "1.0.0"