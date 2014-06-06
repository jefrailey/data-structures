import pytest
import proper_parentheticals


def test_open():
    a_string = "(hello( my good friend)"
    assert proper_parentheticals.parentheticals(a_string) == -1


def test_closed():
    a_string = "(hello( my good friend)))"
    assert proper_parentheticals.parentheticals(a_string) == 1


def test_balanced_proper():
    a_string = "(hello( my good friend))"
    assert proper_parentheticals.parentheticals(a_string) == 0


def test_balanced_improper():
    a_string = ")helo (hello( my good friend)"
    answer = u"You've got all the right pieces in all the wrong places."
    assert proper_parentheticals.parentheticals(a_string) == answer
