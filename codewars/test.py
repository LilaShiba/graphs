meow3= """
...
SG.
...
""".strip('\n')

meow = [[1,0,0],[1,0,0],[1,0,0]]
meow2 = [ y for x in meow for y in x]
meow2 = ','.join(map(str,meow2))


print(meow2)
