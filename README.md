[![ci](https://github.com/ChargeStorm/unittest-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/ChargeStorm/unittest-learning/actions/workflows/ci.yml)
[![docs](https://img.shields.io/badge/Documentation-latest-blue)](https://chargestorm.github.io/unittest-learning/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
![GitHub License](https://img.shields.io/github/license/ChargeStorm/unittest-learning)

# About

A repository of examples and inspiration for extending the users toolbox when writing unittests.

While the examples are written in Python, the concepts are applicable to any language that supports unit testing.

For people that are more into Python, some examples are implemented with both Pythons built in `unittest` framework as well as the third party `pytest` framework to show the differences and similarities between the two.

In the future the documentation will be shared on a Github Pages site, but for now you can clone the repository and build the documentation locally.

Start by install uv:

```bash
pip install uv
```

Then run mkdocs serve to build and serve the documentation locally:

```bash
uv run mkdocs serve
```

The documentation will be available at http://127.0.0.1:8000/ during serving.
