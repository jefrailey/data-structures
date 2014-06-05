import linked_list as LL
import sys
# import pytest


def test_init_LinkedList():
    linked_list = LL.LinkedList()
    assert type(linked_list) == LL.LinkedList


def test_init_Node():
    value = u'test'
    node = LL.Node(value)
    assert type(node) == LL.Node
    assert node.value == value


def test_insert():
    linked_list = LL.LinkedList()
    value = u'test'
    linked_list.insert(value)
    assert linked_list.head_node.value == value
    #    val = u"test"
    #    linked_list = LL.LinkedList()  # Do we need a linked list with pre-existing items to prove that inser() inserts object at head?
    #    linked_list.insert(val)
    #    assert linked_list.display()[0:5] == val


def test_pop():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.pop() == u"test_val_3"


def test_size():
    linked_list = LL.LinkedList()
    assert linked_list.size() == 0
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.size() == 3


def test_search():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.search(u"test_val_2").value == u"test_val_2"


def test_remove_first():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_1")
    linked_list.remove(node)
    assert linked_list.__str__() == "(test_val_3, test_val_2)"


def test_remove_random():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    node = linked_list.search(u"test_val_2")
    linked_list.remove(node)
    assert linked_list.__str__() == "(test_val_3, test_val_1)"


def test_print():
    linked_list = LL.LinkedList()
    linked_list.insert(u"test_val_1")
    linked_list.insert(u"test_val_2")
    linked_list.insert(u"test_val_3")
    assert linked_list.__str__() == "(test_val_3, test_val_2, test_val_1)"
