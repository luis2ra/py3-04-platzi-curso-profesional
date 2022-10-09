# class 14: generadores
'''
Un ejemplo de "Generator expression

'''

print ("class 14: demo of generator expression")
my_list = [0,1,4,7,9,10]

my_second_list = [x**2 for x in my_list]  # List comprehension
my_second_gen = (x**2 for x in my_list)  # Generator expression

print(my_list)
print(my_second_list)
print(my_second_gen)
for element in my_second_gen:
    print(element)
