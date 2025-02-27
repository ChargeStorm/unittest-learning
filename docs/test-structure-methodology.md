# Test structure methodology

This section will cover different methodologies for structuring tests. The goal is to make tests easier to read and understand, and to make it easier to write tests that are maintainable and scalable.

## Given, When, Then

The Given, When, Then (GWT) test structure is a way to organize tests in a way that makes them easier to read and understand. The structure is as follows:

1. **Given**: Set up the initial state of the system under test (SUT).
2. **When**: Perform the action that you want to test.
3. **Then**: Check that the expected result has occurred.

### Example

```python
def test_addition():
    # Given
    x = 1
    y = 2

    # When
    result = x + y

    # Then
    assert result == 3
```

## Arrange, Act, Assert

The Arrange, Act, Assert (AAA) test structure is another way to organize tests. The structure is as follows:

1. **Arrange**: Set up the initial state of the system under test (SUT).
2. **Act**: Perform the action that you want to test.
3. **Assert**: Check that the expected result has occurred.

### Example

```python
def test_addition():
    # Arrange
    x = 1
    y = 2

    # Act
    result = x + y

    # Assert
    assert result == 3
```

## Conclusion

Both the GWT and AAA test structures are useful ways to organize tests. The choice of which structure to use will depend on personal preference and the specific requirements of the test. The most important thing is to be consistent in a project and to make sure that tests are easy to read and understand.
