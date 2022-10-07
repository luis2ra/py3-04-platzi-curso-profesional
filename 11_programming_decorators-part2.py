# class 11: programming decorators (example)

def with_custom_message(message):
    def with_message(func):
        print(f"{message}: ")
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return with_message


@with_custom_message("Hello")
def multiply(a, b):
    print(f"The result of {a} * {b} = {a * b}")


def run():
    print("class 11: programming decorators (other example)")
    multiply(3, 5)


if __name__ == '__main__':
    run()
