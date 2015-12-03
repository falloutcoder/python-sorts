"""
|-----------------------------------------------------------|
|                        Shell Sort                         |
|-----------------------------------------------------------|
|Type                        ||  In-place comparison sort   |
|Worst case performance      ||  O(n2)                      |
|Best case performance       ||  O(n log2 n)                |
|Average case performance    ||  depends on gap sequence    |
|Worst case space complexity ||  O(n) total, O(1) auxiliary |
|-----------------------------------------------------------|
"""

from decorators import timethis


@timethis
def shell_sort(array):
    mid = len(array) / 2
    while mid:
        for i in range(len(array)):
            j = i
            temp = array[i]
            while j >= mid and array[j-mid] > temp:
                array[j] = array[j - mid]
                j -= mid
            array[j] = temp
        mid = mid/2 if mid/2 else (0 if mid == 1 else 1)
    return array
