import pytest
from hypothesis import given, strategies, assume

from fizzbuzz import fizzbuzz


@given(strategies.integers())
def test_fizzbuzz_number(number):
    assume(number > 0)
    assume(not number % 3 == 0 and not number % 5 == 0)
    assert fizzbuzz(number) == number


@given(strategies.integers())
def test_fizzbuzz_fizz(number):
    assume(number > 0)
    assume(number % 3 == 0 and not number % 5 == 0)
    assert fizzbuzz(number) == "Fizz"


@given(strategies.integers())
def test_fizzbuzz_buzz(number):
    assume(number > 0)
    assume(number % 5 == 0 and not number % 3 == 0)
    assert fizzbuzz(number) == "Buzz"


@given(strategies.integers())
def test_fizzbuzz_fizzbuzz(number):
    assume(number > 0 and number % 5 == 0 and number % 3 == 0)
    assert fizzbuzz(number) == "FizzBuzz"


@given(strategies.integers())
def test_fizzbuzz_error(number):
    assume(number < 1)
    with pytest.raises(ValueError) as excinfo:
        fizzbuzz(number)
    assert "BAD INPUT" in str(excinfo.value)
