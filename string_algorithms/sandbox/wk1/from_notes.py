def make_trie(patterns):
    tree = dict()
    tree[0] = {}
    idx = 0

    for word in patterns:
        current = tree[0]
        for letter in word:
            if letter in current.keys():
                current = current[tree[letter]]
            else:
                # set level for current letter
                current[letter] = idx
                # set next level to empty
                tree[idx] = {}
                # set current key to idx and value as blank
                current = tree[idx]
                # increase level
                idx+=1
    return tree

print(make_trie(['bork', 'boof']))
