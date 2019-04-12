import unittest
import ssort

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(ssort.s_sort([23,324,2,4,654,23,3,2,1]),[1, 2, 2, 3, 4, 23, 23, 324, 654])
        self.assertEqual(ssort.s_sort([1,1,1,1]),[1,1,1,1])
        self.assertEqual(ssort.s_sort([1]),[1])
if __name__ == '__main__':
    unittest.main()
