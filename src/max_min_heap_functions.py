class MaxMinHeap:
    def __init__(self, array: list):
        pass

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


# Utility functions
def parent(i):
    """
    :param i: the index of a Node
    :return: The Node's parent
    """
    if i == 0:
        raise IndexError("Tried to find the parent of root")
    return i / 2  # python floors the result be default


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
