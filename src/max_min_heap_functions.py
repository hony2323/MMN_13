import math


class MaxMinHeap:
    def __init__(self, array: list):
        self.array = array  # This array is used to implement the heap
        self.heap_size = len(self.array)

    def heapify(self, i):
        """
        make changes in a certain branch to order the items under a node correctly
        :param i: node to heapify
        """
        # Get sons and grandsons (lr is the left son of the right son)
        l = left(i)
        r = right(i)
        ll = left(l)
        rl = right(l)
        lr = left(r)
        rr = right(r)
        depth = depth_of(i)

        # I want to save duplication of code, so I store even the comparison function
        if depth % 2 == 0:
            comp = lambda x, y: x > y
        else:
            comp = lambda x, y: x < y

        if (not self._index_valid(l)) and (not self._index_valid(r)):  # no sons
            # no need to heapify anymore
            return

        # get the best valid index out of the sons and grandsons
        best_index = self._get_index_with_comp([i, l, r, ll, rl, lr, rr], comp)

        # swap and continue if needed
        # continue is not needed if 'i' is best, nor swap
        if best_index != i:
            tmp = self.array[i]
            self.array[i] = self.array[best_index]
            self.array[best_index] = tmp
            # call heapify again
            self.heapify(best_index)

    def _get_index_with_comp(self, indices: list, comp: callable):
        """
        get the most compatible index of comp
        (assuming the first index is valid)
        :param indices: list of indices to compare
        :param comp: comparison function
        :return: the most compatible index of comp
        """
        if len(indices) == 0:
            raise AttributeError("indices is empty")
        best_index = indices[0]
        for i in indices[1:]:
            if self._index_valid(i):
                if comp(i, best_index):
                    best_index = i
        return best_index

    def build_heap(self):
        """
        iterate the heap from the last item that is not at the last depth
        and start heapifing backwards
        """
        self.heap_size = len(self.array)
        start = int(self.heap_size / 2)  # first none last depth item
        for i in range(start, 0):
            self.heapify(i)

    def heap_extract_max(self):
        """
        extracts the max item in the heap (which is the first one)
        :returns: the max item in the list
        """
        # if there are no items then error
        if self.heap_size < 1:
            raise IndexError("heap is empty, can't extract")

        # get the max item
        max_item = self.array[0]

        # swap the last item with the first and decrease size of heap
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1

        # heapify the new item to it's right place
        if self.heap_size > 1:  # else heapify is unnecessary
            self.heapify(0)
        return max_item

    def heap_extract_min(self):
        """
        extracts the min item and
        :returns: the min item
        """
        # if there are no items then error
        if self.heap_size < 1:
            raise IndexError("heap is empty, can't extract")

        min_index = 0
        l = 1  # left son
        r = 2  # right son

        # get the minimum index out of the three nodes (check existing also)
        if self._index_valid(l) and self.array[l] < self.array[min_index]:
            min_index = l
        if self._index_valid(r) and self.array[r] < self.array[min_index]:
            min_index = r
        # get min item
        min_item = self.array[min_index]

        # swap the last item with the min and decrease size of heap
        self.array[min_index] = self.array[self.heap_size - 1]
        self.heap_size -= 1

        # heapify the new item to it's right place
        if self.heap_size > 1:  # else heapify is unnecessary
            self.heapify(min_index)
        return min_item

    def heap_insert(self, key):
        """
        insert the new value correctly
        :param key: new value to insert
        """
        # Add the new key to the heap and increase size
        if self.heap_size < len(self.array):
            self.array[self.heap_size] = key
        else:
            self.array.append(key)
        self.heap_size += 1

        # Heapify every parent of the new item
        i = self.heap_size - 1
        while i > 0:
            self.heapify(parent(i))
            i -= 1

    def heap_delete(self, i):
        # i can't be deleted from heap
        if self.heap_size < 1:
            raise IndexError("heap is empty, can't extract")
        if i > self.heap_size - 1:
            raise IndexError(f"i ({i}) is bigger then heap_size ({self.heap_size})")

        # save item, swap with last item, decrease size
        item = self.array[i]
        self.array[i] = self.array[self.heap_size - 1]
        self.heap_size -= 1

        if self.heap_size > 1:
            self.heapify(i)
        return item

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
