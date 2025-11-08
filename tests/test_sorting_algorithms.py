import pytest

from sorting_algorithms import Bubble_sort, Heap_sort, Merge_sort, Quick_sort


@pytest.mark.parametrize(
    "array,expected_array",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]),
        ([10000000, 0, -1, 20000000, 3], [-1, 0, 3, 10000000, 20000000]),
        ([20, 20, 1, 1, 3], [1, 1, 3, 20, 20]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-1, 2, 10, -10, 99], [-10, -1, 2, 10, 99]),
    ],
)
class TestSort:
    def test_heap_sort(self, array, expected_array):
        assert Heap_sort.heap_sort(array) == expected_array

    def test_merge_sort(self, array, expected_array):
        assert Merge_sort.merge_sort(array) == expected_array

    def test_bubble_sort(self, array, expected_array):
        assert Bubble_sort.Bubble_sort(array) == expected_array

    def test_quick_sort(self, array, expected_array):
        assert Quick_sort.quick_sort(array) == expected_array
