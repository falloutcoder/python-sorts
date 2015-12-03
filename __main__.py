#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import os
import sys
import glob
import random
import argparse
import importlib

from tabulate import tabulate


def sort_algos(sample, sample_size, no_of_times, sample_range):
    pretty_print = lambda char, count: (print("{}".format(char*count)))
    current_dir = os.path.dirname(os.path.realpath(__file__))

    sorting_algos = glob.glob("{}/*_sort.py".format(current_dir))
    sorting_algos = [x.split('/')[-1][:-3] for x in sorting_algos]

    time_taken = [['Algorithm Name', 'Time Taken (Less Is Better!!)'], ]
    for algo in sorting_algos:
        module = importlib.import_module(algo)
        time_taken.append([algo.title().replace('_', ' '),
                           "{0:.20f} sec".format(getattr(module, algo)(array=sample[:],
                                                                       repeat=no_of_times).time)])
    pretty_print('|', 50)
    print(
        "Sorting Algorithms Ran!\nArray Details And Algorithms Summary As Follow")
    pretty_print('|', 50)
    pretty_print('-', 50)
    print("Length Of Array: {}".format(sample_size))
    print("Range Of Numbers In Array: 0 to {}".format(sample_range-1))
    print("Number Of Times Array Were Sorted: {}".format(no_of_times))
    pretty_print('-', 50)
    print(tabulate(sorted(time_taken, key=lambda x: x[1], reverse=True),
                   headers='firstrow', tablefmt="fancy_grid"))


def run():
    """
    Main Function to execute sorting algorithms
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size",
                        type=int,
                        help="Size of array to be sorted",
                        default=1000)
    parser.add_argument("-l", "--loop",
                        type=int,
                        help="Number of times array sorting should be repeated",
                        default=1)
    parser.add_argument("-r", "--range",
                        type=int,
                        help="Max range of number that should be present in array",
                        default=None)
    args = parser.parse_args()

    size = args.size
    repeat = args.loop
    max_range = args.range if args.range else size

    # Generate sample which will be sorted by all algorithms
    sample = []
    try:
        sample = random.sample(range(max_range), size)
    except ValueError:
        print("Provided values range has to be greater than sample size")
        return None
    # Run all sorting algorithms
    sort_algos(sample, size, no_of_times=repeat, sample_range=max_range)

if __name__ == "__main__":
    run()
