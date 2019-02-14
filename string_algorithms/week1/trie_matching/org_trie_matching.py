# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.isLeaf = False

def solve (text, n, patterns):
	trie = make_trie(patterns)
	# result = []
	# root = Node()
	#
	# for pattern in patterns:
	# 	currentNode = root
	# 	# creates tuple with counter and i and c
	# 	for i, c in enumerate(pattern):
	# 		if c not in currentNode.next:
	# 			currentNode.next[c] = Node()
	# 		if i == len(pattern) -1:
	# 			currentNode.next[c].isLeaf = True
	# 		else:
	# 			currentNode = currentNode.next[c]
	#
	# 	for i in range(len(text)):
	# 		idx = 1
	# 		currentNode = root
	# 		while idx < len(text):
	# 			c = text[idx]
	# 			if c not in currentNode.next: break
	# 			currentNode = currentNode.next[c]
	# 			if currentNode.isLeaf:
	# 				result.append(i)
	# 				break
	# 			idx += 1
	# 	return result

	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
