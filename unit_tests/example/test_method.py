import unittest
import method

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(method.function(['meow','mew','borking', 'borks', 'wof']),['mew', 'wof', 'meow', 'borks', 'borking'], 'some type message')
        self.assertEqual(bsort.bubble_sort(['love', 'I', 'pizzas']),['I', 'love', 'pizzas'])


if __name__ == '__main__':
    unittest.main()
