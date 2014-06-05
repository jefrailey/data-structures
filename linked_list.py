class LinkedList(object):
    def __init__(self, head_node=None):
        self.head_node = head_node
        pass

    def insert(self, val):
        if self.head_node:
            self.head_node = Node(val, self.head_node)
        else:
            self.head_node = Node(val)

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.the_next
            return value

    def size(self):
        if self.head_node:
            size = 1
            node = self.head_node
            while True:
                if node.the_next:
                    size += 1
                    node = node.the_next
                else:
                    break
            return size
        else:
            return 0

    def search(self, val):
        if self.head_node:
            node = self.head_node
            while True:
                if node.the_next:
                    if node.value == val:
                        return node
                    node = node.the_next
                else:
                    return None

    def remove(self, node):
        if self.head_node:
            prev_node = None
            cur_node = self.head_node
        while True:
            if cur_node == node:
                if prev_node is None:
                    self.head_node = node.the_next
                    break
                else:
                    prev_node.the_next = cur_node.the_next
                    break
            else:
                prev_node, cur_node = cur_node, cur_node.the_next

    def __str__(self):
        node = self.head_node
        if not node:
            return "()"
        output = "(%s" % node.value
        node = node.the_next
        while node.value:
            output = "%s, %s" % (output, node.value)
            if node.the_next:
                node = node.the_next
            else:
                break
        output = "%s)" % output
        return output

class Node(object):
    def __init__(self, value, the_next=None):
        self.value = value
        self.the_next = the_next


linked_list = LinkedList()
linked_list.insert(u"test_val_1")
linked_list.insert(u"test_val_2")
linked_list.insert(u"test_val_3")
print(linked_list)
