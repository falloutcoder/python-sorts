# coding: utf-8
"""
|------------------------------------------------------------|
|                     Insertion Sort                         |
|------------------------------------------------------------|
|Type                        ||  In-place stable sort        |
|Worst case performance      ||  O(n2) comparisons, swaps    |
|Best case performance       ||  Ω(n) comparisons, O(1) swaps|
|Average case performance    ||  O(n2) comparisons, swaps    |
|Worst case space complexity ||  O(n) total, O(1) auxiliary  |
|------------------------------------------------------------|
"""

from decorators import timethis


@timethis
def insertion_sort(array):
    size = len(array)
    for index in range(1, size):
        val = array[index]
        position = index

        while position > 0 and array[position-1] > val:
            array[position] = array[position-1]
            position = position-1

        array[position] = val
    return array
