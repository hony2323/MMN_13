import math


class MaxMinHeap:
    def __init__(self, array: list):
        self.array = array  # This array is used to implement the heap

    def heapify(self, i):
        pass

    def build_heap(self):
        pass

    def heap_extract_max(self):
        pass

    def heap_extract_min(self):
        pass

    def heap_insert(self, key):
        pass

    def heap_delete(self, i):
        pass

    def _index_valid(self, i) -> bool:
        """
        Is the index in range of the array length
        """
        return 0 <= i < len(self.array)


# Utility functions
def parent(i):
    """
    :param i: the index of a Node
    :return: The Node's parent
    """
    if i == 0:
        raise IndexError("Tried to find the parent of root")
    return int(i / 2)  # python floors the result be default when converting to int


def left(i):
    """
    :param i: the index of a Node
    :return: The Node's left son
    """
    return 2 * i


def right(i):
    """
    :param i: the index of a Node
    :return: The Node's right son
    """
    return 2 * i + 1


def depth_of(i):
    """
    :returns the depth of i in the heap
    """
    return int(math.log(i, base=2))  # python floors the result be default when converting to int
