import math


class MaxMinHeap:
    def __init__(self, array: list):
        self.array = array  # This array is used to implement the heap
        self.heap_size = len(self.array)

    def heapify(self, i):
        """
        if the depth is even: seek max item and swap if needed and recursive call
        if the depth is odd: seek min item and swap if needed and recursive call
        """
        # Get sons and depth
        r = right(i)
        l = left(i)
        depth = depth_of(i)

        if depth % 2 == 0:  # depth is even
            if self._index_valid(l) and self.array[l] > self.array[i]:  # is left son is valid and larger
                max_index = l
            else:
                max_index = i
            if self._index_valid(r) and self.array[r] > self.array[max_index]:  # is right son is valid and larger
                max_index = r
            if max_index != i:  # if index i is max then swap is not needed. else swap is needed and continuation
                # commit swap
                tmp = self.array[i]
                self.array[i] = self.array[max_index]
                self.array[max_index] = tmp
                # call heapify again
                self.heapify(max_index)
        else:
            if self._index_valid(l) and self.array[l] < self.array[i]:  # is left son is valid and smaller
                min_index = l
            else:
                min_index = i
            if self._index_valid(r) and self.array[r] < self.array[min_index]:  # is right son is valid and smaller
                min_index = r
            if min_index != i:  # if index i is min then swap is not needed. else swap is needed and continuation
                # commit swap
                tmp = self.array[i]
                self.array[i] = self.array[min_index]
                self.array[min_index] = tmp
                # call heapify again
                self.heapify(min_index)

    def build_heap(self):
        """
        iterate the heap from the last item that is not at the last depth
        and start heapfing backwards 
        :return:
        """
        self.heap_size = len(self.array)
        start = int(self.heap_size / 2)  # first none last depth item
        for i in range(start, 0):
            self.heapify(i)

    def heap_extract_max(self):
        pass

    def heap_extract_min(self):
        pass

    def heap_insert(self, key):
        pass

    def heap_delete(self, i):
        pass

    # Private functions
    def _index_valid(self, i) -> bool:
        """
        Is the index in range of the array length
        """
        return 0 <= i < self.heap_size


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
    :returns: the depth of i in the heap
    """
    return int(math.log(i, base=2))  # python floors the result be default when converting to int
