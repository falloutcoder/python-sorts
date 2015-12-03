"""
|-----------------------------------------------------------|
|                       Quick Sort                          |
|-----------------------------------------------------------|
|Type                        ||  Comparison sort            |
|Worst case performance      ||  O(n2)                      |
|Best case performance       ||  O(n log n) or O(n)         |
|Average case performance    ||  O(n log n)                 |
|Worst case space complexity ||  O(n) or O(log n)           |
|-----------------------------------------------------------|
"""

from decorators import timethis


@timethis
def quick_sort(array):
    def _sort(array):
        # Actual Quick Sort Function
        less = []
        equal = []
        greater = []
        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                else:
                    greater.append(x)
            return _sort(less)+equal+_sort(greater)
        else:
            return array
    # Call the Quick Sort Function
    return _sort(array[:])
