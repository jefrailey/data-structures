import proper_parenthetics as pp

answer = u"All the right pieces in all the wrong places."


def test_open():
    a_string = u"(hello( my good friend)"
    assert pp.parentheticals(a_string) == -1


def test_closed():
    a_string = u"(hello( my good friend)))"
    assert pp.parentheticals(a_string) == 1


def test_balanced_proper():
    a_string = u"(hello( my good friend))"
    assert pp.parentheticals(a_string) == 0


def test_balanced_improper1():
    a_string = u")helo (hello( my good friend)"
    assert pp.parentheticals(a_string) == answer


def test_balanced_improper2():
    a_string = u")()()()helo (hello( my go()()()()od friend)"
    assert pp.parentheticals(a_string) == answer


def test_balanced_improper3():
    a_string = u")helo (hello( my good friend)()()()()"
    assert pp.parentheticals(a_string) == answer


def test_balanced_improper4():
    a_string = u"())(((((((((())))))))))("
    assert pp.parentheticals(a_string) == answer
