import string


class Palindrome:
    def check(self, value):
        """Returns if value is a palindrome

        Args:
            value (str): The string to check

        Raises:
            TypeError: If value provided is not str

        Returns:
            boolean: Returns True or False
        """
        if not isinstance(value, str):
            raise TypeError("Please provide a string arguement")
        return self.__santise(value)[::-1] == self.__santise(value)

    def __santise(self, value):
        return (
            value.translate(str.maketrans("", "", string.punctuation))
            .replace(" ", "")
            .lower()
        )
