def function_to_test(print_argument):
    """
    Function for demonstration purposes.

    This function prints the argument passed to it.
    """
    print(print_argument)


def function_with_error():
    """
    Function for demonstration purposes.

    This function prints an error message to stderr.
    """
    import sys

    print("This is an error message", file=sys.stderr)


class TestCapturingOutput:
    """
    This class demonstrates how to capture stdout and stderr using the capsys fixture from pytest.
    """

    def test_capture_stdout(self, capsys):
        """
        This test captures the stdout output of function_to_test.
        """
        function_to_test("Hello, World!")
        captured = capsys.readouterr()
        assert captured.out == "Hello, World!\n"
        assert captured.err == ""

    def test_capture_stderr(self, capsys):
        """
        This test captures the stderr output of function_with_error.
        """
        function_with_error()
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == "This is an error message\n"

    def test_capture_both_stdout_and_stderr(self, capsys):
        """
        This test captures both stdout and stderr output.
        """
        function_to_test("Output to stdout")
        function_with_error()
        captured = capsys.readouterr()
        assert captured.out == "Output to stdout\n"
        assert captured.err == "This is an error message\n"

    def test_partial_capture(self, capsys):
        """
        This test demonstrates partially capturing output within a specific block of code.
        """
        function_to_test("First message")
        with capsys.disabled():
            print("This will not be captured by capsys")
        function_to_test("Second message")

        captured = capsys.readouterr()
        assert captured.out == "First message\nSecond message\n"
        assert captured.err == ""

    def test_assert_no_output(self, capsys):
        """
        This test ensures there is no output captured when no functions are called.
        """
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
