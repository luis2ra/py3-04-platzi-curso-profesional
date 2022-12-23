# class 08: Ejemplo Closure para request HTTP (version closure)
'''
Reglas para encontrar un "closure"

1. Debemos tener una nested function.
2. La nested function debe referenciar un valor de un scope superior.
3. La función que envuelve a la nested function debe retornarla.

'''
import requests


def request_maker(url: str) -> requests.models.Response:
    def make_request(**kwargs):
        return requests.get(url.format_map(kwargs))

    return make_request


def run():
    postman = request_maker("https://postman-echo.com/get?{key}={val}")
    print(postman(key="hello", val="world"))


if __name__ == '__main__':
    run()
