# VARIABLES

# Variables start with lower case, can't start with numbers
x = 5
print(x)

## Numbers

## Strings


# DATA STRUCTURES
## LISTS
my_list = list([1, 2, 3, 4, 5])
### Slicing
sliced_list = my_list[3:]  ## output is [4, 5]

## SETS
my_set = set(["a", "b", "c"])

## TUPLES (Immutable)
my_tuple = tuple(["a", "b", "c", "d"])


## LIST COMPREHENSIONS
my_double_list = [2 * item for item in my_list]
range_list = list(range(50))
filtered_list = [item for item in range_list if item % 10 == 0]


def clean_word(word):
    return word.replace(".", "").lower()


MY_STRING = "Hello my name is John. I love python"
clean_string_list = [
    clean_word(word) for word in MY_STRING.split() if len(clean_word(word)) > 3
]


## DICTIONARY COMPREHENSIONS
animal_list = [("a", "dog"), ("b", "cat"), ("c", "fish")]
animal_dictionary = dict(animal_list)
print(animal_dictionary)
list(animal_dictionary.items)
