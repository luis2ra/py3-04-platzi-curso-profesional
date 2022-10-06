# class 10: decorator
'''
Syntactic Sugar in Python:

Syntactic sugar is a syntax that allow developers to write code easier, in a “sweety” way.

'''

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje!'

print(mensaje("Luis Alfonso"))
