class PrimeFactors:
    def get(self, value):
        """Returns all prime factors for value

        Args:
            number (int): Input value to find prime factors for

        Returns:
            list: List of prime factors for input value
        """
        if not isinstance(value, int):
            raise TypeError("Please provide an int arguement")
        factors = []
        divisor = 2
        while divisor <= value:
            if value % divisor == 0:
                value = value / divisor
                factors.append(divisor)
            else:
                divisor += 1
        return factors
