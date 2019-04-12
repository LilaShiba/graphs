import unittest
import bsort

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(bsort.bubble_sort(['meow','mew','borking', 'borks', 'wof']),['mew', 'wof', 'meow', 'borks', 'borking'])
        self.assertEqual(bsort.bubble_sort(['love', 'I', 'pizzas']),['I', 'love', 'pizzas'])
    def test_medium(self):
        self.assertEqual(bsort.bubble_sort(['werwerwer','sdfsdfsdf','ewrwegfgrt4 4t435 2345', '235g wer fsd er sdf e', '25 gfs3 235 ']),['werwerwer', 'sdfsdfsdf', '25 gfs3 235 ', '235g wer fsd er sdf e', 'ewrwegfgrt4 4t435 2345'])

if __name__ == '__main__':
    unittest.main()
