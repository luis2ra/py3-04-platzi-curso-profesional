# class 11: programming decorators
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("duration of execution time: ", str(time_elapsed.total_seconds()) + " seconds")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Luis"):
    print("Hola " + nombre)


def run():
    print("class 11: programming decorators")
    random_func()  # función sin argumentos
    suma(6, 3)  # función con dos argumentos enteros
    saludo("Alfonso")  # función con un argumento de tipo cadena


if __name__ == '__main__':
    run()
