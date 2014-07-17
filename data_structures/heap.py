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
        child = self.core[child_index]
        the_parent_index = self._get_p(child_index)
        parent = self.core[the_parent_index]
        if child > parent:
            self.core[child_index], self.core[the_parent_index] = parent, child
            return True
        else:
            return False

    def _get_p(self, child_index):
        u"""Computes the p index from a c index."""
        if child_index:
            return (child_index-1)//2
        else:
            return 0

    def _get_cren(self, p_index):
        u"""Returns a tuple consisting of the two cren of a given p."""
        return (2*p_index+1), (2*p_index+2)

    def _get_sib(self, index):
        parent = self._get_p(index)
        sib = self._get_cren(parent)
        for i in sib:
            if i != index:
                return i

    def push(self, num):
        u"""Adds a vaue to the heap and correctly reorganizes."""
        self.core.append(num)
        self._organize_up()

    def _organize_up(self, num_index=None):
        while num_index is None:
            num_index = len(self.core)-1
        while self._flip_p_c(num_index):
            num_index = self._get_p(num_index)

    def _organize_down(self):
        num_index = 0
        drop_complete = False
        while not drop_complete:
            num_index, drop_complete = self._flip_down(num_index)
        self.core = self.core[:num_index]

    def _flip_down(self, current_index):
        u"""Flips the popped value down through the tree.

        This process continues until the popped value reaches the bottom,
        where it is ready to be removed."""

        current = self.core[current_index]
        left_index, right_index = self._get_cren(current_index)

        # If the current has no children:
        if left_index >= len(self.core) and right_index >= len(self.core):
            if (len(self.core)-1) != current_index:
                self.core[-1], self.core[current_index] = current, self.core[-1]
                self._organize_up(current_index)
            return (len(self.core)-1), True

        # If the current has one child at the left index:
        elif right_index >= len(self.core):
            left = self.core[left_index]
            self.core[left_index], self.core[current_index] = current, left
            return left_index, True

        # Else: The current has two children:
        else:
            left, right = self.core[left_index], self.core[right_index]
            if left >= right:
                self.core[left_index], self.core[current_index] = current, left
                return left_index, False
            elif left < right:
                self.core[right_index], self.core[current_index] = current, right
                return right_index, False

    def pop(self):
        u"""Removes the top value from the heap and correctly reorganizes."""
        try:
            popped_value = self.core[0]
        except IndexError:
            return None
        else:
            self._organize_down()
            return popped_value