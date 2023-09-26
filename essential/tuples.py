# Tuples: ordered, immutable, allows duplicate elements

my_tuple = ("Max", 1, False, "UK")
print(my_tuple)

single_tuple = ("test",)
print(single_tuple)

big_tuple = (my_tuple, single_tuple)
print(big_tuple)
print(big_tuple[0][0])
print(big_tuple.count("test"))
name, age, single, country = my_tuple
print(name, age, single, country)

name, *age_status, country = my_tuple  # unpacking
print(name, age_status, country)