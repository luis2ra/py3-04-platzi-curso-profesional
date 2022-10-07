# class 12: iterators
'''
Los iteradores son una estructura de datos (avanzada) para guardar datos infinitos

Que son los iterables?
Son aquellos objetos/instancias que pueden ser recorridos por un ciclo, por ejemplo, una lista.

'''

# Creando un iterador
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador
print(next(my_iter))  
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))  # Cuando no queda datos, la excepcion StopIteration es elevada