# class 08: nested functions as preview to closures


def main():
    a = 1

    # se define una función dentro de otra función
    def nested():
        print(a)

    nested()  # se llama la función interna


def run():
    print("class 08: nested functions as preview to closures")
    main()


if __name__ == '__main__':
    run()
