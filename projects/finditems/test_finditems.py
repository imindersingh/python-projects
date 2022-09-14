import pytest
from finditems import FindItems


class TestFindItems:
    @pytest.fixture
    def find_items(self):
        return FindItems()

    def test_returns_all_indices_in_list_for_search_value(self, find_items):
        input_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        expected = [[0, 0, 1], [0, 1], [1, 1]]
        search_value = 2
        assert find_items.index_all(input_list, search_value) == expected
