def heapify(a, i):
    pass


def build_heap(a):
    pass


def heap_extract_max(a):
    pass


def heap_extract_min(a):
    pass


def heap_insert(a, key):
    pass


def heap_delete(a, i):
    pass


# Private functions
def _parent(i):
    """
    :param i: the index of a Node
    :return: The Node's parent
    """
    if i == 0:
        raise IndexError("Tried to find the parent of root")
    return i / 2  # python floors the result be default


def _left(i):
    """
    :param i: the index of a Node
    :return: The Node's left son
    """
    return 2 * i


def _right(i):
    """
    :param i: the index of a Node
    :return: The Node's right son
    """
    return 2 * i + 1
