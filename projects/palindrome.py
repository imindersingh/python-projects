import string
import pytest

def palindrome(value):
    if not isinstance(value, str):
        raise TypeError("Please provide a string arguement")    
    return santise(value)[::-1] == santise(value)

def santise(value):
    return value.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()

def main():
    value = input("Enter value: ")
    is_palindrome = palindrome(value)
    print(is_palindrome)
    
@pytest.mark.parametrize("value,expected", [
    ("dad! D ? a D d-a-D", "daddaddad"),
    ("DAD", "dad"),
    ("    da   d", "dad"),
    ("!dad", "dad"),
])

def test_santise(value, expected):
    assert santise(value) == expected

def test_raises_exception_on_non_string_arguements():
    with pytest.raises(TypeError):
        palindrome(2)

if __name__ == "__main__":
    main()