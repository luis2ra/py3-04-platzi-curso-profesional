# class 16: sets
'''
Sets: Una colección desordenada de elementos únicos e inmutables.

'''

my_set = {3, 4, 5}
print("my_set = ", my_set)
# {3, 4, 5}

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 = ", my_set2)
# {False, True, "Hola", 23.3}

my_set3 = {3, 3, 2}
print("my_set3 = ", my_set3)
# {3, 2}

empty_set = {}  # Esto es dict por defecto
print(type(empty_set))
# <class 'dict'>

empty_set = set()  # Esto si genera un set por defecto
print(type(empty_set))
# <class 'set'>

my_list = [1, 1, 2, 3, 4, 4, 5]
my_list_to_set =  set(my_list)
print("my_list_to_set = ", my_list_to_set)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_tuple_to_set = set(my_tuple)
print("my_tuple_to_set = ", set(my_tuple))

# ERROR!!!
# my_set4 = {[1, 2, 3], 4}  # Esto da un error, contiene una lista (y por definicion, es mutable)
