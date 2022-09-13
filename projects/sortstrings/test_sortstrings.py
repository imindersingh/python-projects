import pytest
from sortstrings import SortStrings


class TestSortStrings:
    @pytest.fixture
    def sort_strings(self):
        """Returns a SortStrings instance"""
        return SortStrings()

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("FLOWER apple hi Bird window duCK", "apple Bird duCK FLOWER hi window"),
            ("a D c", "a c D"),
            ("APPle1 LIGHT3 cat54", "APPle1 cat54 LIGHT3"),
        ],
    )
    def test_can_sort_strings(self, sort_strings, input_str, expected):
        assert sort_strings.sort(input_str) == expected

    def test_raises_exception_for_non_string_arguement(self, sort_strings):
        with pytest.raises(TypeError) as exception:
            sort_strings.sort(3)
        assert str(exception.value) == "Please provide a string of words for input"
