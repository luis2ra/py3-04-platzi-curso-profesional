# class 08: Revision de otra fuente para los closures
'''
Un closure no es más que una función la cual puede generar, de forma dinámica, 
a otra función. Además, que esta nueva función puede acceder a las variables 
locales aun cuando la primera haya finalizado.

fuente: https://codigofacilito.com/articulos/closures-python
'''
def saludar_usuario(username):
    mensaje = 'Hola ' + username

    def saludar():
        print(mensaje)

    return saludar


def run():
    saludo = saludar_usuario("luis")   
    saludo()


if __name__ == '__main__':
    run()
