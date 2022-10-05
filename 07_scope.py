# class 07: scope

x = 6  # global scope
z = 3  # other global scope
'''
cada scope tiene sus propias variables!!!
'''

def my_func():
    y = 5
    z = 7

    def my_internal_function():
        z = 2
        print(z)
    
    my_internal_function()
    print(y)  # local scope OK
    print(x)
    print(z)


def my_other_function():
    print(x)


def run():
    print("class 07: scope")
    my_func()
    my_other_function()
    # print(y)
    print(x)
    print(z)

if __name__ == '__main__':
    run()