from src.max_min_heap_functions import MaxMinHeap, right, left


def validate_max_min_heap(mmh, i, depth):
    if not mmh.index_valid(i):
        return True
    if not validate_max_min_item(mmh, i, i, depth):
        return False
    return validate_max_min_heap(mmh, left(i), depth + 1) and validate_max_min_heap(mmh, right(i), depth + 1)


def validate_max_min_item(mmh: MaxMinHeap, original_i, curr_i, original_depth):
    if not mmh.index_valid(curr_i):
        return True
    if original_depth % 2 == 0:
        comp = lambda x, y: x > y
    else:
        comp = lambda x, y: x < y

    if comp(mmh[curr_i], mmh[original_i]):
        return False

    return validate_max_min_item(mmh, original_i, right(curr_i), original_depth) and \
        validate_max_min_item(mmh, original_i, left(curr_i), original_depth)
