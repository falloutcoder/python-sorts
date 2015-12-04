## Python Sorting Algorithms
Comparison of sorting algorithms in Python. Run algorithms on arrays of user specified lengths and analyze time taken by each algorithm to sort the array. All algorithms are tested so be confident that arrays are sorted correctly.

Python's builtin 'sorted' method uses Timsort algorithm created by Tim Peters, The man behind python's easter egg (import this). Though in these tests 'sorted' function has upper hand on other algorithms because of being a builtin function, but still you have to admit Tim Peters is awesome. Get started ...
``` sh
git clone https://github.com/falloutcoder/python-sorts.git sorts
```
## Requirements:
Currently there is only one dependency 'Tabulate', To print summary table for algorithms in better form.

Run following command to install it:

``` sh
pip install -r requirements.txt
```

## Run Tests Before Using

``` sh
$ python sorts/test.py
Testing shell_sort
Testing insertion_sort
Testing quick_sort
Testing bubble_sort
Testing tim_sort
Testing merge_sort
Testing selection_sort
.
----------------------------------------------------------------------
Ran 1 test in 0.009s

OK

```

On some machines below error is expected:
``` sh
ImportError: Import by filename is not supported.
```
## Usage

Default run without any arguments

```sh
$ python sorts
||||||||||||||||||||||||||||||||||||||||||||||||||
Sorting Algorithms Ran!
Array Details And Algorithms Summary As Follow
||||||||||||||||||||||||||||||||||||||||||||||||||
--------------------------------------------------
Length Of Array: 1000
Range Of Numbers In Array: 0 to 999
Number Of Times Array Were Sorted: 1
--------------------------------------------------
╒══════════════════╤═════════════════════════════════╕
│ Algorithm Name   │ Time Taken (Less Is Better!!)   │
╞══════════════════╪═════════════════════════════════╡
│ Bubble Sort      │ 0.03952097892761230469 sec      │
├──────────────────┼─────────────────────────────────┤
│ Insertion Sort   │ 0.02639412879943847656 sec      │
├──────────────────┼─────────────────────────────────┤
│ Selection Sort   │ 0.02118921279907226562 sec      │
├──────────────────┼─────────────────────────────────┤
│ Merge Sort       │ 0.00230097770690917969 sec      │
├──────────────────┼─────────────────────────────────┤
│ Shell Sort       │ 0.00182795524597167969 sec      │
├──────────────────┼─────────────────────────────────┤
│ Quick Sort       │ 0.00158691406250000000 sec      │
├──────────────────┼─────────────────────────────────┤
│ Tim Sort         │ 0.00016212463378906250 sec      │
╘══════════════════╧═════════════════════════════════╛

```

### Avaiable Parameters
```sh
$ python sorts -h
usage: sorts [-h] [-s SIZE] [-l LOOP] [-r RANGE]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Size of array to be sorted
  -l LOOP, --loop LOOP  Number of times array sorting should be repeated
  -r RANGE, --range RANGE
                        Max range of number that should be present in array

$ python sorts -s 4500 -r 60000
||||||||||||||||||||||||||||||||||||||||||||||||||
Sorting Algorithms Ran!
Array Details And Algorithms Summary As Follow
||||||||||||||||||||||||||||||||||||||||||||||||||
--------------------------------------------------
Length Of Array: 4500
Range Of Numbers In Array: 0 to 59999
Number Of Times Array Were Sorted: 1
--------------------------------------------------
╒══════════════════╤═════════════════════════════════╕
│ Algorithm Name   │ Time Taken (Less Is Better!!)   │
╞══════════════════╪═════════════════════════════════╡
│ Bubble Sort      │ 0.76305413246154785156 sec      │
├──────────────────┼─────────────────────────────────┤
│ Insertion Sort   │ 0.51503109931945800781 sec      │
├──────────────────┼─────────────────────────────────┤
│ Selection Sort   │ 0.45219206809997558594 sec      │
├──────────────────┼─────────────────────────────────┤
│ Merge Sort       │ 0.01211810111999511719 sec      │
├──────────────────┼─────────────────────────────────┤
│ Shell Sort       │ 0.01209998130798339844 sec      │
├──────────────────┼─────────────────────────────────┤
│ Quick Sort       │ 0.00762200355529785156 sec      │
├──────────────────┼─────────────────────────────────┤
│ Tim Sort         │ 0.00092196464538574219 sec      │
╘══════════════════╧═════════════════════════════════╛

```