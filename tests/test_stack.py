import pytest
from data_structures import stack


@pytest.fixture(scope='function')
def _make_stack():
    a_stack = stack.Stack()
    a_stack.push(u"value1")
    a_stack.push(u"value2")
    a_stack.push(u"value3")
    return a_stack


def _make_stack_alt_vals():
    u"""Instantiate a Stack of vals that evaluate False."""
    a_stack = stack.Stack()
    a_stack.push(0)
    a_stack.push(None)
    a_stack.push(False)
    return a_stack


def test_stack_init(_make_stack):
    u"""Test the init method on Stack class."""
    assert isinstance(_make_stack, stack.Stack)


def test_stack_init_alt_vals():
    u"""Test the init method on a Stack class."""
    alt_val_stack = _make_stack_alt_vals()
    assert isinstance(alt_val_stack, stack.Stack)


def test__data__init():
    u"""Test the init method on Data class."""
    a_data = stack.Data(u"a value")
    assert isinstance(a_data, stack.Data)
    assert a_data.value == u"a value"


def test_push(_make_stack):
    u"""Test a single push on the Stack class."""
    assert _make_stack.head_data.value == u"value3"


def test_push_alt_vals():
    u"""Test a single push on a Stack of vals that evaluate False."""
    alt_val_stack = _make_stack_alt_vals()
    assert alt_val_stack.head_data.value is False


def test_push_no_value(_make_stack):
    u"""Test push() Data without value."""
    with pytest.raises(TypeError):
        _make_stack.push()


def test_pop_multiple(_make_stack):
    u"""Test multiple pops on the Stack class."""
    _make_stack.pop()
    assert _make_stack.head_data.value == u"value2"
    _make_stack.pop()
    assert _make_stack.head_data.value == u"value1"
    _make_stack.pop()
    assert _make_stack.head_data is None
    with pytest.raises(LookupError):
        _make_stack.pop()


def test_pop_multiple_alt_vals():
    u"""Test multiple pops on a Stack of vals that evaluate False."""
    alt_val_stack = _make_stack_alt_vals()
    alt_val_stack.pop()
    assert alt_val_stack.head_data.value is None
    alt_val_stack.pop()
    assert alt_val_stack.head_data.value is 0
    alt_val_stack.pop()
    assert alt_val_stack.head_data is None
    with pytest.raises(LookupError):
        alt_val_stack.pop()
