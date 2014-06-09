def parentheticals(a_string):
    _close = a_string.count(u")")
    _open = a_string.count(u"(")
    if _open > _close:
        return 1
    elif _open < _close:
        return -1
    elif _open == _close:
        _count = 0
        for letter in a_string:
            if _count > 0:
                return -2
            elif letter == u"(":
                _count -= 1
            elif letter == u")":
                _count += 1
        else:
            return 0
