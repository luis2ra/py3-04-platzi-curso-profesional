# class 13: the fibonacci sequence (challenge)

class FibonacciIter:
    def __init__(self, max=1):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux > self.max:
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux  # swapping in python
            self.counter += 1
            return self.n2  # que es el mismo valor de self.aux (la suma) 


def run():
    print("class 13: the fibonacci sequence")
    user_value = int(input("Ingresa el valor máximo para generar los números de Fibonacci: "))
    fibonacci = FibonacciIter(user_value)
    for element in fibonacci:
        print(element)


if __name__ == '__main__':
    run()
