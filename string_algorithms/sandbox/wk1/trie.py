def build_trie(patterns):
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
    #print(tree)
    return tree



def solve(text, n, patterns):
    # hold index values of matches
    result = []
    # build trie
    trie = build_trie(patterns)

    n = len(text)
    # for all letters in text + 1
    for i in range(n):
        # if there is a match from current letter to end of text in trie
        if prefix_trie_matching(text[i:], trie):
            # add index value to results
            result.append(i)

    return result


def prefix_trie_matching(text, trie):
    # index counter
    idx = 0
    # symbol is first letter
    symbol = text[idx]
    # current is {'A': 1, 'G': 5}
    # first dictonary that is nested
    current = trie[0]

    while True:
        # if at end, return true
        if not current:
            return True
        elif symbol in current.keys():
            # follow nodes that are in text
            current = trie[current[symbol]]
            # increase counter to represent index
            idx = idx + 1
            # if letters are left to check
            if idx < len(text):
                # symbol is next letter
                symbol = text[idx]
            else:
                # end
                symbol = '@'
        else:
            return False




trie = solve('AATCGGGTTCAATCGGGGT',2,['ATCG', 'GGGT'])
print(trie)






# def prefix_trie_matching(text, trie):
#     idx = 0
#     symbol = text[idx]
#     current = trie[0]
#
#     while True:
#         if not current:
#             return True
#         elif symbol in current.keys():
#             current = trie[current[symbol]]
#             idx = idx + 1
#             if idx < len(text):
#                 symbol = text[idx]
#
#             else:
#                 symbol = '@'
#         else:
#             return False
# print(prefix_trie_matching('ATC', trie))
