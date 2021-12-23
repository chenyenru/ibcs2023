# algorithms/searching.py

from typing import List
import random


def sequential_search(value: int, array: List[int]) -> int:
    for idx, val in enumerate(array):
        if val == value:
            return idx
    return None


def binary_search(value: int, array: List[int], start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(array)-1
    # Find the midpoint of the (sub)array
    mid = start + (end - start) // 2

    if end >= start:
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            # Search through right subarray
            return binary_search(value, array, start=mid+1, end=end)
        else:
            # Search through left subarray
            return binary_search(value, array, start=start, end=mid-1)
    else:
        return None


def create_random_list(min: int = 0, max: int = 100, size: int = 150):
    data = []
    for i in range(size):
        data.append(random.randint(min, max))
    return data


def test_sequential_search(value: int, array: List[int]):
    idx = sequential_search(value, array)
    if idx is None:
        print(f"Did not find {value}")
    else:
        print(f"{value} found at index {idx}")


def test_binary_search(value: int, array: List[int]):
    array.sort()
    idx = binary_search(value, array)
    if idx is None:
        print(f"Did not find {value}")
    else:
        print(f"{value} found at index {idx}")


def main():
    data = create_random_list(55, 110, 50)
    value = 73
    data[10] = value
    print(data)
    # the returned index may be different
    test_sequential_search(value, data)
    test_binary_search(value, data)


if __name__ == "__main__":
    main()
