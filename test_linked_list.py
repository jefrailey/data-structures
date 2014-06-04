import linked_list as LL
# import pytest


def test_init_LinkedList():
    linked_list = LL.LinkedList()
    assert type(linked_list) == LL.LinkedList


def test_init_Node():
    value = u'test'
    node = LL.Node(value)
    assert type(node) == LL.Node
    assert node.value() == value


def test_insert():
    val = u"test"
    linked_list = LL.LinkedList()  # Do we need a linked list with pre-existing items to prove that inser() inserts object at head?
    linked_list.insert(val)
    assert linked_list.display()[0:5] == val


def test_pop():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.pop() == u"test_val_3"


def test_size():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.size() == 3


def test_search():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.search(u"test_val_2") == u"test_val_2_node"


def test_remove():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_1")
    linked_list.remove(node)
    assert linked_list.display() == (u"test_val_3", u"test_val_2")


def test_print():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_1")
    linked_list.remove(node)
    assert linked_list.display() == (u"test_val_3", u"test_val_2")