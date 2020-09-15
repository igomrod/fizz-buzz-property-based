def fizzbuzz(number: int):
    if number < 1:
        raise ValueError("BAD INPUT")
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number

