from hash_table import HashTable


def _make_wordlist():
    with open('/usr/share/dict/words', 'r') as f:
        wordlist = []
        for word in f.readlines():
            wordlist.append(word)
    return wordlist


def test_hash_one_letter_key():
    size = 8
    char = "a"
    h = HashTable(size)
    assert h.hash(char) == (ord(char) % size)


def test_hash_two_letter_key():
    size = 8
    char = "ab"
    h = HashTable(size)
    assert h.hash(char) == (
        sum([ord(c) for c in char]) % size
        )

def test_set_one_letter_key():
    size = 8
    chars = "habcdefg"
    h = HashTable(size)
    for c in chars:
        h.set(c, 63)
    assert h.table == [[(letter, 63)] for letter in chars]
