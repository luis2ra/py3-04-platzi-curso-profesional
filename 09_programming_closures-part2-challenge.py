# class 09: programming closures (challenge)
'''
This closure returns a function that returns
the division of a number x by n

'''

def make_division_by(n):
    def divide_to(x):
        return x / n
    return divide_to


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 =  make_division_by(5)
    print(division_by_5(100))


if __name__ == '__main__':
    run()
