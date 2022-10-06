# class 08: closures
'''
Reglas para encontrar un "closure"

1. Debemos tener una nested function.
2. La nested function debe referenciar un valor de un scope superior.
3. La función que envuelve a la nested function debe retornarla.

'''

def main():
    a = 1

    # se define la función nested()
    def nested():
        print(a)

    return nested  # se retorna la invocación de la función interna


def run():
    print("class 08: closures")
    my_func =  main()
    my_func()


if __name__ == '__main__':
    run()
