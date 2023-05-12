import os
import json
from max_min_heap_functions import *
from validation import validate_max_min_heap

ROOT_DIR = ""  # fill if there are errors with the dir


if __name__ == '__main__':
    root_dir = ROOT_DIR or os.path.dirname(os.path.abspath(__file__))
    for i in range(1, 4):
        with open(os.path.join(root_dir, f"examples/example{i}.json")) as f:
            d = json.load(f)
        print(f"before: {d}")
        mmh = MaxMinHeap(d)
        mmh.build_heap()
        print(f"after: {mmh.array}")
        print(validate_max_min_heap(mmh, 0, 0))
