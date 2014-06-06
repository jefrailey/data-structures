def parentheticals(a_string):
    if a_string.count(u"(") > a_string.count(u")"):
        return -1
    elif a_string.count(u"(") < a_string.count(u")"):
        return 1
    elif a_string.count(u"(") == a_string.count(u")"):
        open_count = 0
        closed_count = 0
        for letter in a_string:
            if closed_count > open_count:
                return u"All the right pieces in all the wrong places."
            elif letter == u"(":
                open_count += 1
            elif letter == u")":
                closed_count += 1
        else:
            return 0
