class Heap(object):
    def __init__(self):
        u"""Initializes with a list that contains """
        self.core = [u'_TOP_']

    def __len__(self):
        return len(self.core)

    def __getitem__(self,key):
        return self.core[key+1]

    def _flip_parent_child(self,child_index, invert=False):
        u"""Flips parent/child if child is greater than parent.

        Unless invert is set to True, in which case it does the opposite.
        Returns True if switch occured, False otherwise."""
        return bool

    def _get_parent(self,child_index):
        return (child_index-1)//2

    def _get_children(self,parent_index):
        return (2*parent_index+1),(2*parent_index+2)

    def push(self,num):
        u"""Adds a vaue to the heap and correctly reorganizes."""
        pass

    def pop(self):
        u"""Removes the top value from the heap and correctly reorganizes."""
        return popped_value