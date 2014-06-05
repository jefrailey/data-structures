import pytest
import stack

def test__stack__init():
    u"""Test the init method on Stack class"""
    a_stack = stack.Stack()
    assert isinstance(a_stack, stack.Stack)

def test__data__init():
    u"""Test the init method on Data class"""
    a_data = stack.Data(u"a value")
    assert isinstance(a_data, stack.Data)
    assert a_data.value == u"a value"

def test_push():
    a_stack = stack.Stack()
    a_data = stack.Data(u"value1")
    a_stack.push(a_data)
    assert a_stack.head_data.value == u"value1"

def test_push_multiple():
    a_stack = stack.Stack()
    a_data = stack.Data(u"value1")
    a_stack.push(a_data)
    b_data = stack.Data(u"value2")
    a_stack.push(b_data)
    c_data = stack.Data(u"value3")
    a_stack.push(c_data)
    assert a_stack.head_data.value == u"value3"

def test_push_multiple():
    a_stack = stack.Stack()
    a_data = stack.Data(u"value1")
    a_stack.push(a_data)
    b_data = stack.Data(u"value2")
    a_stack.push(b_data)
    c_data = stack.Data(u"value3")
    a_stack.push(c_data)
    a_stack.pop()
    assert a_stack.head_data.value == u"value2"
    a_stack.pop()
    assert a_stack.head_data.value == u"value1"
    with pytest.raises(LookupError):
        a_stack.pop()


