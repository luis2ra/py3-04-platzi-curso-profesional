# class 09: programming closures
'''
La idea de este programa es hacer un multiplicador de string, por ejemplo:

si el string es "Hola" y el numero es 3, la respuesta seria HolaHolaHola

'''


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Luis"))

    repeat_10 =  make_repeater_of(10)
    print(repeat_10("Alfonso"))

    repeat_3 = make_repeater_of(3)
    # print(repeat_3(9))  # esto es para validar el uso de la sentencia assert


if __name__ == '__main__':
    run()
