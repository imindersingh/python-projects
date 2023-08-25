import math

print("Hellow world")

# Variables
name = "Iminder"
print(name)
age = 20
height = 250.5
human = True

# Check Data Type
print(type(name))

# Type Casting
print("Your age is: " + str(age))
print("Your height is: " + str(height))

# String Methods
print(len(name))
print(name.find("I"))  # Find index
print(name.isalpha())  # Check for alpha chars
print(name * 3)  # Multiply String

# Inputs
# input_name = input("What is your name? ")
# input_age = int(input("What is your age? "))

# Maths
pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
# print(pow(pi))
print(math.sqrt(420))
print(max(1, 2, 4))
print(min(1, 2, 4))
