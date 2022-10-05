def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()  # borra espacios en blanco y pasar todo a minuscula
    return string == string[::-1]

def run():
    print("class 06: practicando el tipado estatico")
    print(is_palindrome("Ana"))
    print(is_palindrome("Luis"))
    print(is_palindrome(10000))

if __name__ == "__main__":
    run()
