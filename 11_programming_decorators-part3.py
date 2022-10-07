# class 11: programming decorators (example)

def text_with_borders(func):
    def wrapper(text):
        print(" " + "_" * (1 + len(text)))
        print("/" + "_" * (len(text)) + "/|")
        print("|" + " " * (len(text)) + "||")
        func("|" + text + "||")
        print("|" + "_" * (len(text)) + "|/")
    return wrapper


@text_with_borders
def imprime(texto):
    print(texto)


def run():
    print("class 11: programming decorators (other example)")
    text = input("Escribe un texto: ")
    imprime(text)


if __name__ == '__main__':
    run()
