import os
import json
from max_min_heap_functions import *


def check_max_min_heap(mmh: MaxMinHeap, i):
    if i >= mmh.heap_size:
        return True
    if depth_of(i) % 2 == 0:
        if mmh.array[i] < mmh.array[left(i)] or mmh.array[i] < mmh.array[right(i)]:
            return False
    else:
        if mmh.array[i] > mmh.array[left(i)] or mmh.array[i] > mmh.array[right(i)]:
            return False
    return check_max_min_heap(mmh, left(i)) and check_max_min_heap(mmh, right(i))


if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_dir, "examples/example1.json")) as f:
        d = json.load(f)
    print(f"before: {d}")
    mmh = MaxMinHeap(d)
    mmh.build_heap()
    print(f"after: {mmh.array}")
    print(check_max_min_heap(mmh, 0))
