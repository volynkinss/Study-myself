# when dividing parametr by 3 and 5 display FizzBuzz, only by 3 -> Fizz, only by 5 -> Buzz, if not divisible by 3 or 5 display parametr
# my_code:
def fizz_buzz(number: int) -> int:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


fizz_buzz(3)
# on video:
