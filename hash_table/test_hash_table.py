from hash_table import HashTable


def _make_wordlist():
    with open('/usr/share/dict/words', 'r') as f:
        wordlist = []
        for word in f.readlines():
            wordlist.append(word)
    return wordlist

