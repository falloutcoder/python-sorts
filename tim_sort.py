"""
|-----------------------------------------------------------|
|                         Tim Sort                          |
|-----------------------------------------------------------|
|Created By Tim Roberts      ||  Python's Builtin Sort      |
|Worst case performance      ||  O(n log n)                 |
|Best case performance       ||  O(n)                       |
|Average case performance    ||  O(n log n)                 |
|Worst case space complexity ||  O(n)                       |
|-----------------------------------------------------------|
"""

from decorators import timethis


@timethis
def tim_sort(array):
    return sorted(array)
