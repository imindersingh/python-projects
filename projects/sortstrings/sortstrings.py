class SortStrings:
    def sort(self, value):
        """Returns a alphabetically sorted string of words, ignoring case

        Args:
            value (str): String of words to sort

        Raises:
            TypeError: If input is not str

        Returns:
            str: String of words
        """
        if not isinstance(value, str):
            raise TypeError("Please provide a string of words for input")
        return " ".join(sorted(value.split(), key=str.casefold))
