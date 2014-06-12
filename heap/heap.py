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

    def _organize_up(self):
        num_index = len(self.core)-1
        # num = self.core[num_index]
        while self._flip_p_c(num_index):
            num_index = self._get_p(num_index)

    def _organize_down(self):
        num_index = 0
        drop_complete = False
        while not drop_complete:
            num_index, drop_complete = self._flip_down(num_index)
        self.core = self.core[:num_index] + self.core[num_index+1:]

    def _flip_down(self, parent_index):
        parent = self.core[parent_index]
        left_index, right_index = self._get_cren(parent_index)
        if left_index >= len(self.core) and right_index >= len(self.core):
            nephews = self._get_cren(self._get_sib(parent_index))
            left_index, right_index = nephews
            try:
                left = self.core[left_index]
            except IndexError:
                left = None
            try:
                right = self.core[right_index]
            except IndexError:
                right = None
            if left >= right and left is not None:
                self.core[left_index], self.core[parent_index] = parent, left
                return left_index, True
            elif left < right and right is not None:
                self.core[right_index], self.core[parent_index] = parent, right
                return right_index, True
            return parent_index, True
        elif left_index >= len(self.core):
            right = self.core[right_index]
            self.core[right_index], self.core[parent_index] = parent, right
            return right_index, False
        elif right_index >= len(self.core):
            left = self.core[left_index]
            self.core[left_index], self.core[parent_index] = parent, left
            return left_index, False
        else:
            left, right = self.core[left_index], self.core[right_index]
            if left >= right:
                self.core[left_index], self.core[parent_index] = parent, left
                return left_index, False
            elif left < right:
                self.core[right_index], self.core[parent_index] = parent, right
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