# class 17: sets operations

my_set1 = {3, 4, 5}
print("my_set1 = ", my_set1)
my_set2 = {5, 6, 7}
print("my_set2 = ", my_set2)

# Union
my_set3 = my_set1 | my_set2
print("my_set3 = ", my_set3)

# Intersection
my_set4 = my_set1 & my_set2
print("my_set4 = ", my_set4)

# Difference
my_set5 = my_set1 - my_set2
print("my_set5 = ", my_set5)
my_set6 = my_set2 - my_set1
print("my_set6 = ", my_set6)

# symmetrical difference
my_set7 = my_set1 ^ my_set2
print("my_set7 = ", my_set7)
