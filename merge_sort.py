"""
|-----------------------------------------------------------|
|                       Merge Sort                          |
|-----------------------------------------------------------|
|Type                        ||  Comparison base stable sort|
|Worst case performance      ||  O(n log n)                 |
|Best case performance       ||  O(n log n) or O(n)         |
|Average case performance    ||  O(n log n)                 |
|Worst case space complexity ||  O(n) or O(log n)           |
|-----------------------------------------------------------|
"""

from decorators import timethis


@timethis
def merge_sort(array):
    def _sort(array):
        # Actual Merge Sort Function
        if len(array) == 1:
            return array
        else:
            mid = len(array)/2
            left = _sort(array[:mid])
            right = _sort(array[mid:])

            left_counter, right_counter, counter = 0, 0, 0

            while left_counter < len(left) and right_counter < len(right):
                if left[left_counter] < right[right_counter]:
                    array[counter] = left[left_counter]
                    left_counter += 1
                    counter += 1
                else:
                    array[counter] = right[right_counter]
                    right_counter += 1
                    counter += 1

            remaining = left if left_counter < right_counter else right
            r = left_counter if remaining == left else right_counter

            while r < len(remaining):
                array[counter] = remaining[r]
                r += 1
                counter += 1
            return array
    # Call the Merge Sort Function
    return _sort(array)
