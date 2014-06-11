class Heap(object):
    def __init__(self, invert=False):
        u"""Initializes a max binary heap by default.

        If invert is set to True, then it creates a min heap."""

        self.core = []
        self.invert = invert

    def __len__(self):
        return len(self.core)

    def __getitem__(self,key):
        return self.core[key]

    def _flip_parent_child(self,child_index):
        u"""Flips parent/child if child is greater than parent.

        Unless self.invert is set to True, in which case it does the opposite.
        Returns True if switch occured, False otherwise."""
        return bool

    def _get_parent(self,child_index):
        u"""Computes the parent index from a child index."""
        return (child_index-1)//2

    def _get_children(self,parent_index):
        u"""Returns a tuple consisting of the two children of a given parent."""
        return (2*parent_index+1),(2*parent_index+2)

    def push(self,num):
        u"""Adds a vaue to the heap and correctly reorganizes."""
        pass

    def pop(self):
        u"""Removes the top value from the heap and correctly reorganizes."""
        return popped_value