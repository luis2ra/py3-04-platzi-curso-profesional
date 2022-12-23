def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()  # borra espacios en blanco y pasar todo a minuscula
    return string == string[::-1]

def run():
    print("class 06: practicando el tipado estatico")
    print(is_palindrome("Ana"))
    print(is_palindrome("Luis"))

    '''
    Esta linea genera un error, ya que se pasa un entero

    Se aplica el comando mypy, para detectar este tipo de error, con el flag adecuado
    $ mypy 06_palindrome.py --check-untyped-defs

    Importante agregar el flag "check-untyped-defs"
    '''
    print(is_palindrome(10000)) 

if __name__ == "__main__":
    run()
