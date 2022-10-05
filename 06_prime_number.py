import functools


def is_prime_number(number: int) -> bool:
    my_list = [i for i in range(1, number + 1)]
    divisors = list(filter(lambda x: number % x == 0, my_list))
    # print(divisors)
    return len(divisors) == 1 if number == 1 else len(divisors) == 2

def run():
    print("class 06: challenge")
    print(is_prime_number(1))
    print(is_prime_number(3))
    print(is_prime_number(6))

    # para validar sentencia mypy
    # print(is_prime_number("pepe"))

if __name__ == "__main__":
    run()
