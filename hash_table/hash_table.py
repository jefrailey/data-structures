from math import log


class HashTable(object):
    def __init__(self, size):
        u"""Instantiate a HashTable with size number of buckets.

        If size is not a power of two, then size will be increased to the next
        power of two.
        """
        if size % 2 != 0:
            self.size = 2**(int(log(size, 2)))*2
        else:
            self.size = size
        self.table = [[] for i in xrange(self.size)]

    def hash(self, key):
        u"""Return hashed key."""
        if not isinstance(key, str):
            raise KeyError
        key_sum = 0
        for letter in key:
            key_sum += ord(letter)
        mask = self.size - 1
        return key_sum & mask

    def set(self, key, val):
        u"""Add a value to the hash table."""
        position = self.hash(key)
        sub_list = self.table[position]
        if sub_list != []:
            for ind, pair in enumerate(self.table[position]):
                if pair[0] == key:
                    sub_list.pop(ind)
        sub_list.append((key, val))

    def get(self, key):
        u"""Return the value associated with that key."""
        position = self.hash(key)
        return [val for k, val in self.table[position] if k == key][0]
