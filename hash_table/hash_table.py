class HashTable(object):
    """docstring for HashTable"""
    def __init__(self, size):
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
        position = self.hash(key)
        self.table[position].append((key, val))

    def get(self, key):
        pass