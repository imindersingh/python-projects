import pytest
from palindrome import Palindrome


class TestPalindrome:
    @pytest.fixture
    def palindrome(self):
        """Returns a Palindrome instance"""
        return Palindrome()

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("dad! D ? a D d-a-D", True),
            ("DAD", True),
            ("    da   d", True),
            ("!dad", True),
            ("hello!@!", False),
            ("bsdkljs sdlkjsdl 38", False),
        ],
    )
    def test_santise(self, value, expected, palindrome):
        assert palindrome.check(value) is expected

    def test_raises_exception_on_non_string_arguements(self, palindrome):
        with pytest.raises(TypeError):
            palindrome.check(2)
