# algorithms/sorting.py

from typing import List
from searching import create_random_list


def bubble_sort(array: List[int]) -> None:
    # Create flag to indicate if value
    # has been swapped
    swapped = True
    end = len(array) - 1
    # Keep repeating while swapped is True
    while swapped:
        # We haven't swapped anything in this loop
        # so swapped is false
        swapped = False
        for i in range(end):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        end -= 1


def selection_sort(array: List[int]) -> None:
    for i in range(len(array) - 1):
        # assume i is the smallest index value
        m = i
        # look through all other elements
        for j in range(i, len(array)):
            # If value at j is smaller than value at m
            # set m to j
            if array[j] < array[m]:
                m = j

        # if m is not i, we found a smaller value
        if m != i:
            array[m], array[i] = array[i], array[m]


def insertion_sort(array: List[int]) -> None:
    # bubble sort + selection sort
    for i in range(1, len(array)):
        key = array[i]  # so that the key doesn't change
        j = i - 1
        # while we find values greater than key
        # swap j and j+1
        # here we can see j+1 as i
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def merge_sort(array: List[int], left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(array) - 1

    if right <= left:
        return

    # integer divide by 2
    mid = (right + left) // 2

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)


def merge(array: List[int], left: int, mid: int, right: int):
    i = left  # starting index of the left array
    j = mid + 1  # starting index of the right array
    k = 0
    # create a temporary array for easier understanding
    tmp = [0] * (right - left + 1)

    while i <= mid and j <= right:
        # copying from the left subarray
        if array[i] < array[j]:
            tmp[k] = array[i]
            i += 1
        else:
            # copying from the right subarray
            tmp[k] = array[j]
            j += 1
        k += 1
    while i <= mid:
        # in case that the left array has any remaining value
        tmp[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        # in case that the right array has any remaining value
        tmp[k] = array[j]
        j += 1
        k += 1

    # Copy temporary array back into original array
    k = 0
    while left + k <= right:
        array[left + k] = tmp[k]
        k += 1


def main() -> None:
    data = create_random_list()
    print(data)
    # bubble_sort(data)
    # selection_sort(data)
    # insertion_sort(data)
    merge_sort(data)
    print(data)


if __name__ == "__main__":
    main()
