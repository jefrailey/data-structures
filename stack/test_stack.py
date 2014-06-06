import pytest
import stack


@pytest.fixture(scope='function')
def _make_stack():
    a_stack = stack.Stack()
    a_stack.push(u"value1")
    a_stack.push(u"value2")
    a_stack.push(u"value3")
    return a_stack


def test__stack__init(_make_stack):
    u"""Test the init method on Stack class"""
    assert isinstance(_make_stack, stack.Stack)


def test__data__init():
    u"""Test the init method on Data class"""
    a_data = stack.Data(u"a value")
    assert isinstance(a_data, stack.Data)
    assert a_data.value == u"a value"


def test_push(_make_stack):
    u"""Test a single push on the Stack class"""
    assert _make_stack.head_data.value == u"value3"


def test_push_no_value(_make_stack):
    u"""Test push() Data without value."""
    with pytest.raises(TypeError):
        _make_stack.push()


def test_pop_multiple(_make_stack):
    u"""Test multiple pops on the Stack class"""
    _make_stack.pop()
    assert _make_stack.head_data.value == u"value2"
    _make_stack.pop()
    assert _make_stack.head_data.value == u"value1"
    _make_stack.pop()
    assert _make_stack.head_data is None
    with pytest.raises(LookupError):
        _make_stack.pop()
