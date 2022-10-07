# class 12: iterators
'''
Protocolo de los iteradores:

Para constuir un iterador, debemos tener una clase que contenga dos metodos importantes: __iter__ y __next__

'''

class EvenNumbers:
    '''
    Clase que implementa un iterador
    de todos los números pares, o los números
    pares hasta un máximo
    '''

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


def run():
    print("class 12: iterators")
    even_numbers = EvenNumbers(100)
    for element in even_numbers:
        print("nro. par: ", element)


if __name__ == '__main__':
    run()
