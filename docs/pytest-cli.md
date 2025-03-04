# Pytest CLI Tips

`pytest` provides a versatile and powerful command-line interface (CLI) with numerous options that can help tailor test execution to your needs. This guide covers some of the most useful `pytest` CLI options, including filtering tests, capturing output, running tests in parallel, and more.

## Filtering Tests

### `-k`: Run Tests Matching Specific Expressions

Use the `-k` option to run tests that match a given expression. This is useful when you want to run a subset of tests based on their names or any substring.

```bash
pytest -k "expression"
```

Examples:

- Run tests with "data" in their name:

  ```bash
  pytest -k "data"
  ```

- Run tests that have `test_create` in their name:

  ```bash
  pytest -k "test_create"
  ```

You can also use logical expressions:

```bash
pytest -k "test_method or test_function"
```

or

```bash
pytest -k "test_method and not test_function"
```

## Capturing Output

### `-s`: Disable Output Capturing

By default, `pytest` captures all output (e.g., print statements) during test execution. Use the `-s` option to disable this behavior and allow output to be displayed in real-time.

```bash
pytest -s
```

## Parallel Execution

### `pytest-xdist`: Run Tests in Parallel

`pytest-xdist` is a plugin that allows you to run tests in parallel using multiple CPU cores.

### Installation

```bash
pip install pytest-xdist
```

### Usage

Use the `-n` option to specify the number of CPU cores to use for parallel test execution:

```bash
pytest -n 4
```

This will distribute the tests across 4 CPU cores, running them concurrently and thus reducing the overall testing time.

## Markers

### `-m`: Run Tests with Specific Markers

Use the `-m` option to run tests that are marked with a specific keyword or marker.

```bash
pytest -m "marker"
```

Examples:

- Run tests marked with `slow`:

  ```bash
  pytest -m "slow"
  ```

- Run tests excluding `slow` marked tests:

  ```bash
  pytest -m "not slow"
  ```

## Fail Fast

### `-x`: Stop After First Failure

Use the `-x` option to stop test execution immediately after the first failure.

```bash
pytest -x
```

### `--maxfail`: Specify Number of Failures Before Stopping

Use the `--maxfail` option to specify the maximum number of failures allowed before stopping the test run.

```bash
pytest --maxfail=3
```

## Disabling Warnings

### `-p no:warnings`: Disable Warnings

Use the `-p no:warnings` option to disable warnings during test execution.

```bash
pytest -p no:warnings
```

## Running Specific Tests

### Running Specific Test Files or Directories

You can specify particular test files or directories to run:

```bash
pytest tests/test_file.py
pytest tests/test_directory/
```

### Running Specific Test Classes or Functions

You can also run specific test classes or test functions within files:

```bash
pytest tests/test_file.py::TestClass
pytest tests/test_file.py::TestClass::test_function
```

## Conclusion

These `pytest` CLI options and plugins can greatly enhance your testing experience by providing fine-grained control over test selection, output capturing, parallel execution, and more. By leveraging these tools, you can optimize your testing workflow and improve efficiency.
