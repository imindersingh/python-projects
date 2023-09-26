# Lists: ordered, mutable, allows duplicate elements

my_list = ["bab", "aksj", "d"]
print(my_list)

myList2 = list()
print(myList2)

print(my_list[0])
print(my_list[-1])  # Last item in the list

for i in my_list:
    print(i)

if "bab" in my_list:
    print(str(True))
else:
    print(str(False))

new_list = [1, 2, 3, 4, 5]
print(sorted(new_list))
print(new_list * 2)  # duplicates list
print(new_list[::2])  # prints every 2nd element from the beginning
print(new_list[::-1])  # reverse list

print([i * i for i in new_list])  # list comprehension

