class Heap(object):

    u"""An object that represents a max binary heap."""

    def __init__(self):
        self.core = []

    def push(self, num):
        u"""Add a vaue to the heap and reorganize the heap."""
        self.core.append(num)
        self._organize_up()

    def pop(self):
        u"""Remove the top value from the heap and reorganize the heap."""
        try:
            popped_value = self.core[0]
        except IndexError:
            return None
        else:
            self._organize_down()
            return popped_value

    def _flip_parent_child(self, child_index):
        u"""Swap parent with child if child is greater; return False if not."""
        child = self.core[child_index]
        parent_index = self._get_parent(child_index)
        parent = self.core[parent_index]
        if child > parent:
            self.core[child_index], self.core[parent_index] = parent, child
            return True
        return False

    def _get_parent(self, child_index):
        u"""Compute the parent index from a child index."""
        if child_index:
            return (child_index-1)//2
        return 0

    def _get_children(self, p_index):
        u"""Return a tuple consisting of the two children of a given p."""
        return (2*p_index+1), (2*p_index+2)

    def _organize_up(self, num_index=None):
        if num_index is None:
            num_index = len(self.core)-1
        while self._flip_parent_child(num_index):
            num_index = self._get_parent(num_index)

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
        left_index, right_index = self._get_children(current_index)

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

    def __len__(self):
        return len(self.core)

    def __getitem__(self, key):
        return self.core[key]
