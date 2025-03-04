# Coverage Reporting in Python

Code coverage is a measure used to describe the degree to which the source code of a program is tested by a particular test suite. `coverage.py` is a popular tool for measuring code coverage in Python projects.

## Installation

To get started with coverage reporting, you need to install `coverage.py`. Additionally, if you are using `pytest`, there is a plugin called `pytest-cov` that integrates coverage reporting with pytest.

You can install these packages via pip:

```bash
pip install coverage pytest-cov
```

## Basic Usage with Coverage.py

### Running Coverage with pytest

To run your tests with coverage using `pytest`, use the following command:

```bash
pytest --cov=myproject
```

In this command:

- `--cov=myproject` specifies the module or package to measure for coverage.

### Generating the Report

After running your tests with coverage, you can generate a report. The most common reports are text, HTML, and XML reports.

#### Text Report

To generate a text report in the terminal:

```bash
pytest --cov=myproject --cov-report=term
```

#### HTML Report

To generate an HTML report that you can view in a browser:

```bash
pytest --cov=myproject --cov-report=html
```

Open the generated `htmlcov/index.html` file in your web browser to view the report.

#### XML Report

To generate an XML report, suitable for use with CI tools:

```bash
pytest --cov=myproject --cov-report=xml
```

## Integrating with pytest

### Configuration

To simplify running tests with coverage using pytest, you can add configuration to your `pyproject.toml` file.

#### pyproject.toml

Create or modify `pyproject.toml`:

```toml
[tool.pytest.ini_options]
addopts = [
    "--cov=myproject",
    "--cov-report=term",
    "--cov-report=html"
]
```

In this configuration:

- `--cov=myproject` specifies the module or package to measure for coverage.
- `--cov-report=term` generates a text report in the terminal.
- `--cov-report=html` generates an HTML report.

### Running Tests with Coverage

After configuration, simply run pytest to execute tests with coverage reporting:

```bash
pytest
```

## Ignoring Code from Coverage

In some cases, you might want to exclude specific lines or files from the coverage report. You can use a special comment `# pragma: no cover` to indicate that a line should not be considered when measuring coverage.

### Ignoring Specific Lines

```python
# myproject/module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):  # pragma: no cover
    return a * b
```

### Ignoring Entire Files

You can also configure `coverage.py` to omit entire files via the `pyproject.toml` configuration file.

Create or modify `pyproject.toml` file:

```toml
[tool.coverage.run]
omit = [
    "myproject/some_file_to_ignore.py"
]
```

## Integrating with Azure Pipelines

You can also integrate test coverage reporting into Azure Pipelines. Below is an example configuration for running tests with coverage and generating reports in an Azure Pipelines job.

```yaml
jobs:
  - job: "test"
    displayName: "Run tests"
    steps:
      - checkout: self
      - bash: |
          curl -LsSf https://astral.sh/uv/install.sh | sh
        displayName: "Install uv"
      - bash: |
          uv pip install pytest-azurepipelines
          uv run pytest --cov=myproject --cov-report xml --cov-report html --junitxml junit/test-results.xml
        displayName: "Run tests"
      - task: reportgenerator@5
        inputs:
          reports: "**/coverage.xml"
          targetdir: "cover"
          publishCodeCoverageResults: true
        displayName: "Generate code coverage report"
```

In this configuration:

- The `bash` step installs `uv`.
- The `bash` step runs `pytest` with coverage options, generating both XML and HTML reports.
- The `reportgenerator` task collects the coverage reports and uploads them to Azure Pipelines.

## Conclusion

Code coverage is an essential part of ensuring your tests adequately cover your codebase. Tools like `coverage.py` and `pytest-cov` make it easy to measure and report on code coverage. By integrating coverage reporting into your testing workflow, you can better understand which parts of your code are being tested and identify areas that may need additional tests.

Integrating coverage reporting into CI tools like Azure Pipelines further enhances your development workflow by providing continuous feedback on your code coverage metrics.
