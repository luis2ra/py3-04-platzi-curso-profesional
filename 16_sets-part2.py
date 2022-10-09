# class 16: sets
'''
Sets: Una colección desordenada de elementos únicos e inmutables.

'''

my_set = {1, 2, 3}
print("my_set = ", my_set)

# agrega un elemento
my_set.add(4)
print("my_set = ", my_set)

# agrega elementos multiples a un set
my_set.update([1, 2, 5])
print("my_set = ", my_set)

# otra forma de agregar elementos multiples a un set, en este caso una tupla y otro set
my_set.update((1, 7, 2), {6, 8})
print("my_set = ", my_set)


# borrar un elemento de existente usando "discard"
my_set.discard(1)
print("my_set appling discard = ", my_set)

# borrar un elemento de existente usando "remove"
my_set.remove(2)
print("my_set appling remove = ", my_set)

# borrar un elemento de existente usando "discard"
my_set.discard(11)
print("my_set appling discard = ", my_set)

# borrar un elemento aleaotorio usando "pop"
my_set.pop()
print("my_set appling pop = ", my_set)

# borrar un elemento de existente usando "remove" (Esto genera un error!!!)
my_set.remove(12)
print("my_set appling remove = ", my_set)

# con esta sentencia, limpia todo el set
my_set.clear()
print("my_set = ", my_set)
