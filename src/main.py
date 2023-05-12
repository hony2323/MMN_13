import os
import json
from max_min_heap_functions import *

ROOT_DIR = ""  # fill if there are errors with the dir


def check_max_min_heap(mmh: MaxMinHeap, i):
    if i >= mmh.heap_size:
        return True
    if depth_of(i) % 2 == 0:
        if (left(i) < mmh.heap_size and mmh.array[i] < mmh.array[left(i)]) or (
                right(i) < mmh.heap_size and mmh.array[i] < mmh.array[right(i)]):
            return False
    else:
        if (left(i) < mmh.heap_size and mmh.array[i] > mmh.array[left(i)]) or (
                right(i) < mmh.heap_size and mmh.array[i] > mmh.array[right(i)]):
            return False
    return check_max_min_heap(mmh, left(i)) and check_max_min_heap(mmh, right(i))


if __name__ == '__main__':
    root_dir = ROOT_DIR or os.path.dirname(os.path.abspath(__file__))
    for i in range(1, 4):
        with open(os.path.join(root_dir, f"examples/example{i}.json")) as f:
            d = json.load(f)
        print(f"before: {d}")
        mmh = MaxMinHeap(d)
        mmh.build_heap()
        print(f"after: {mmh.array}")
        print(check_max_min_heap(mmh, 0))
