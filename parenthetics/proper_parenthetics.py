def parentheticals(a_string):
    if a_string.count(u"(") > a_string.count(u")"):
        return -1
    elif a_string.count(u"(") < a_string.count(u")"):
        return 1
    elif a_string.count(u"(") == a_string.count(u")"):
        pass
