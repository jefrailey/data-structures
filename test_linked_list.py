import linked_list as LL


def test_init_LinkedList():
    u"""Assert that a LinkedList object is instantiated."""
    linked_list = LL.LinkedList()
    assert type(linked_list) == LL.LinkedList


def test_init_Node():
    u"""Assert that a Node object is instantiated."""
    value = u'test'
    node = LL.Node(value)
    assert type(node) == LL.Node
    assert node.value == value


def test_insert():
    u"""Assert that .insert() inserts a Node at the head of a LinkedList."""
    linked_list = LL.LinkedList()
    value = u'test'
    linked_list.insert(value)
    assert linked_list.head_node.value == value


def test_pop():
    u"""Assert that .pop() returns the value of the Node at the head."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.pop() == u"test_val_3"


def test_size():
    u"""Assert that .size() returns the number of Nodes in a LinkedList."""
    linked_list = LL.LinkedList()
    assert linked_list.size() == 0
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.size() == 3


def test_search_first():
    u"""Assert that .search() returns the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.search(u"test_val_3").value == u"test_val_3"


def test_search_middle():
    u"""Assert that .search() returns the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.search(u"test_val_2").value == u"test_val_2"


def test_search_last():
    u"""Assert that .search() returns the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.search(u"test_val_1").value == u"test_val_1"


def test_remove_last():
    u"""Assert that .remove() removes the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_1")
    linked_list.remove(node)
    assert linked_list.__str__() == u"(test_val_3, test_val_2)"


def test_remove_first():
    u"""Assert that .remove() removes the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_3")
    linked_list.remove(node)
    assert linked_list.__str__() == u"(test_val_2, test_val_1)"


def test_remove_middle():
    u"""Assert that .remove() removes the desired Node."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_2")
    linked_list.remove(node)
    assert linked_list.__str__() == u"(test_val_3, test_val_1)"


def test_print():
    u"""Assert that print(LinkedList) displays the LinkedList Node values."""
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.__str__() == u"(test_val_3, test_val_2, test_val_1)"
