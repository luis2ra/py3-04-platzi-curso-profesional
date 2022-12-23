# class 08: Ejemplo Closure para request HTTP (clase original)
'''
Reglas para encontrar un "closure"

1. Debemos tener una nested function.
2. La nested function debe referenciar un valor de un scope superior.
3. La función que envuelve a la nested function debe retornarla.

'''
import requests


class RequestMaker:
    def __init__(self, base_url: str) -> None:
        self.url = base_url

    def request(self, **kwargs) -> requests.models.Response:
        return requests.get(self.url.format_map(kwargs))


def run():
    postman = RequestMaker("https://postman-echo.com/get?{key}={val}")
    print(postman.request(key="hello", val="world"))


if __name__ == '__main__':
    run()
