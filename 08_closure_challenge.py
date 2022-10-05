# class 08: challenge using a closure
'''
Reglas para encontrar un "closure"

1. Debemos tener una nested function.
2. La nested function debe referenciar un valor de un scope superior.
3. La función que envuelve a la nested function debe retornarla.

'''

def make_multiplier(x):

    # se define la función multiplier()
    def multiplier(n):
        return x * n

    return multiplier  # se retorna la invocación de la función multiplier


def run():
    print("class 08: challenge using a closure")

    times10 = make_multiplier(10)
    print(times10(3))

    times4 = make_multiplier(4)
    print(times4(5))

    print(times10(times4(2)))


if __name__ == '__main__':
    run()
