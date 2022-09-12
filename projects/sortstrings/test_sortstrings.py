import pytest
from sortstrings import SortStrings


class TestSortStrings:
    @pytest.fixture
    def sort_strings(self):
        """Returns a SortStrings instance"""
        return SortStrings()

    def test_can_sort_strings(self, sort_strings):
        input_str = "FLOWER apple hi Bird window duCK"
        expected = "apple Bird duCK FLOWER hi window"
        assert sort_strings.sort(input_str) == expected
