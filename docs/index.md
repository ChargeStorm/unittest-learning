# About

This site contains a collection of examples and inspiration for extending the users toolbox when writing unittests.

While the examples are written in Python, the concepts are applicable to any language that supports unit testing.

For people that are more into Python, some examples are implemented with both Pythons built in `unittest` framework as well as the third party `pytest` framework to show the differences and similarities between the two.

## A common definition of a unit test

The definition of unit tests can vary depending on who you ask, which is why it is important to define what a unit test is in the context of this documentation.

Here we've choosen to use the definition from Michael Feathers book [Working Effectively with Legacy Code](https://www.amazon.se/-/en/Michael-Feathers/dp/0131177052).

In short, a test is **not** a unit test if:

> 1. It talks to external resources (e.g. a database, the network, the file system, environment variables…)
> 2. It doesn’t run fast ( < 100ms/test)

!!! info
    The book `Working Effectively with Legacy Code` is available at our office for borrowing.

So from that definition we can conclude that a unit test does not need to be confined to single function or method, but can span multiple functions or methods as long as it does not talk to external resources and runs fast.

Also please remember to always clean up after yourself, if you create a file, remove it, even if the test fails.

We should be able to check out the repository, run the tests without any external resources and be sure that everything is cleaned up afterwards.

## Table of Contents

### Before Starting

- [Test Structure Methodology](test-structure-methodology.md)
- [Package Specific Test Libraries](package-specific-test-libraries.md)
- [Code Coverage](code-coverage.md)
- [Pytest Plugins](pytest-plugins.md)

### Code Examples

- [Assertion](assertion.md)
- [Mocking](mocking.md)
- [Fixtures](fixtures.md)
- [Parametrization](parametrization.md)
- [Markers](markers.md)
- [Exceptions](exceptions.md)
- [Capturing Output](capturing-output.md)
- [Logging](logging.md)
