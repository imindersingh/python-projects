import pytest
from prime_factors import PrimeFactors


class TestPrimeFactors:
    @pytest.fixture
    def prime_factors(self):
        """Returns a PrimeFactors instance"""
        return PrimeFactors()

    def test_can_get_prime_factors(self, prime_factors):
        expected = [2, 3, 3, 5, 7]
        assert prime_factors.get(630) == expected

    def test_prime_number_as_input_returns_itself(self, prime_factors):
        expected = [13]
        assert prime_factors.get(13) == expected

    def test_raises_exception_on_non_string_arguements(self, prime_factors):
        with pytest.raises(TypeError) as exception:
            prime_factors.get("dsdlsdklsk")
        assert str(exception.value) == "Please provide an int arguement"
