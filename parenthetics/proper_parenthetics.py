def parentheticals(a_string):
    if a_string.count(u"(") > a_string.count(u")"):
        return -1
    elif a_string.count(u"(") < a_string.count(u")"):
        return 1
    elif a_string.count(u"(") == a_string.count(u")"):
        open_index = 0
        closed_index = 0
        parens_list = []
        for letter in a_string:
            if letter == u"(" or letter == u")":
                parens_list.append(letter)
        for pos, paren in enumerate(parens_list, 1):
            if paren == u"(":
                open_index += pos
            elif paren == u")":
                closed_index += pos
        if open_index < closed_index:
            return 0
        else:
            return u"You've got all the right pieces in all the wrong places."
