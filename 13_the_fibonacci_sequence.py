# class 13: the fibonacci sequence
import time


class FibonacciIter():

    # def __init__(self):
    #     self.n1 = 0
    #     self.n2 = 1

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
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux  # swapping in python
            self.counter += 1
            return self.n2  # que es el mismo valor de self.aux (la suma) 


def run():
    print("class 13: the fibonacci sequence")
    fibonacci = FibonacciIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)  # esto es un delay para ver los resultados de forma legible        


if __name__ == '__main__':
    run()
