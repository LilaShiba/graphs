example_tests = [
	[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'],
	[
		'XOXOX',
		'OXXOX',
		'XXOXX',
		'XOXOX',
		'OOXOX'],
	[
		'OXOOX',
		'XXOXO',
		'XOXXX',
		'XXOXX',
		'OXXOO'],
	[
		'XXOXO',
		'XOXOX',
		'OXOXO',
		'XOXOX',
		'XXOXX'],# null
	[
		'XXXXX',
		'OOOXO',
		'XXXOX',
		'OOOOO',
		'XXXXX']
]
for i,v in enumerate('\n'.join(v) for v in example_tests):
    print(v)
