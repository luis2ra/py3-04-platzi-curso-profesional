# class 14: generadores
'''
Un generador es un "sugar syntax" de un iterador.
Los generadores son funciones que guardan un estado.
Un generador es un iterador escrito de forma mas simple, osea, mas elegante.

'''


def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n  # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n


a = my_gen()
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) # StopIteration
