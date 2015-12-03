#!/usr/bin/env python
# coding: utf-8
"""
|------------------------------------------------------------|
|                       Bubble Sort                          |
|------------------------------------------------------------|
|Also known as               ||  sinking sort                |
|Worst case performance      ||  О(n2)                       |
|Best case performance       ||  O(n)                        |
|Average case performance    ||  О(n2)                       |
|Worst case space complexity ||  O(1) auxiliary              |
|------------------------------------------------------------|
"""

from decorators import timethis


@timethis
def bubble_sort(array):
    size = len(array)
    for i in range(size):
        for j in range(i+1, size):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array
