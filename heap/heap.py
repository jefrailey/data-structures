class Heap(object):
    def __init__(self, invert=False):
        u"""Initializes a max binary heap by default.

        If invert is set to True, then it creates a min heap."""

        self.core = []
        self.invert = invert

    def __len__(self):
        return len(self.core)

    def __getitem__(self, key):
        return self.core[key]

    def _flip_p_c(self, child_index):
        u"""Flips p/c if c is greater than p.

        Unless self.invert is set to True, in which case it does the opposite.
        Returns True if switch occured, False otherwise."""
        print "Start _flip_p_c"
        child = self.core[child_index]
        parent_index = self._get_p(child_index)
        parent = self.core[parent_index]
        if child > parent:
            self.core[child_index], self.core[parent_index] = parent, child
            return True
        else:
            return False

    def _get_p(self, child_index):
        u"""Computes the p index from a c index."""
        if child_index:
            print "_get_p: {}".format((child_index-1)//2)
            return (child_index-1)//2
        else:
            return 0

    def _get_cren(self, p_index):
        u"""Returns a tuple consisting of the two cren of a given p."""
        return (2*p_index+1), (2*p_index+2)

    def push(self, num):
        u"""Adds a vaue to the heap and correctly reorganizes."""
        self.core.append(num)
        self._organize_up()

    def _organize_up(self):
        num_index = len(self.core)-1
        # num = self.core[num_index]
        while self._flip_p_c(num_index):
            num_index = self._get_p(num_index)
        print self.core

    def pop(self):
        u"""Removes the top value from the heap and correctly reorganizes."""
        return popped_value