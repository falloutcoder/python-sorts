"""
|-----------------------------------------------------------|
|                     Selection Sort                        |
|-----------------------------------------------------------|
|Type                        ||  In-place comparison sort   |
|Worst case performance      ||  O(n2)                      |
|Best case performance       ||  O(n2)                      |
|Average case performance    ||  O(n2)                      |
|Worst case space complexity ||  O(n) total, O(1) auxiliary |
|-----------------------------------------------------------|
"""

from decorators import timethis


@timethis
def selection_sort(array):
    size = len(array)
    for i in range(size):
        smallest = i
        for x in range(i+1, size):
            if array[smallest] > array[x]:
                smallest = x
        array[i], array[smallest] = array[smallest], array[i]
    return array
