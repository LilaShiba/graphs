def make_trie(pattern):
    # {}
    tree = dict()
    # {0: {}}
    tree[0] = {}
    index = 1

    for pattern in patterns:
		# current = { 0:{current} }
        current = tree[0]
        for letter in pattern:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
				# current = { }
				# creates nested dict
				# first round {0: {'a': 1} }
                current[letter] = index
				# creates new dictonary set (row)
				# first round {0: {'a': 1}, 1:{ } }
                tree[index] = {}
				# set current to new dict which is blank
                current = tree[index]
				# next level
                index = index + 1
    return tree



def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)

    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)

    return result


def prefix_trie_matching(text, trie):
    idx = 0
    symbol = text[idx]
    current = trie[0]

    while True:
        if not current:
            return True
        elif symbol in current.keys():
            current = trie[current[symbol]]
            idx = idx + 1
            if idx < len(text):
                symbol = text[idx]
            else:
                symbol = '@'
        else:
            return False




trie = build_trie(['ATAGA', 'ATC', 'GAT'])






def prefix_trie_matching(text, trie):
    idx = 0
    symbol = text[idx]
    current = trie[0]

    while True:
        if not current:
            return True
        elif symbol in current.keys():
            current = trie[current[symbol]]
            idx = idx + 1
            if idx < len(text):
                symbol = text[idx]

            else:
                symbol = '@'
        else:
            return False
print(prefix_trie_matching('ATC', trie))
