import os
import glob
import random
import importlib
import unittest


class SortAlgosTest(unittest.TestCase):

    def setUp(self):
        """
        Common setup to load all sorting modules in current package
        following name convention of endswith('_sort.py'). Imprt 
        """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        sorting_algos = glob.glob("{}/*_sort.py".format(current_dir))
        sorting_algos = [x.split('/')[-1][:-3] for x in sorting_algos]
        modules = [importlib.import_module(algo) for algo in sorting_algos]

        self.sorting_algos = zip(sorting_algos, modules)

    def test_algos_with_sequential_array(self):
        """
        Test a shuffeld sample of 50 numbers. Sorted array contains
        50 numbers in sequence. Strating from 0 to 49
        """
        self.array = random.sample(range(50), 50)
        for algo, module in self.sorting_algos:
            print("Testing {}".format(algo))
            result = getattr(module, algo)(
                array=self.array[:], repeat=1).output
            for index, val in enumerate(range(50)):
                assert val == result[index]


if __name__ == '__main__':
    unittest.main()
