import unittest
import method
# the raincoats

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(method.add(2,2), 4, "output should be 4")

    def test_mild(self):
        self.assertEqual(method.add(2,-2), 0, 'output should be 0')

if __name__ == '__main__':
    unittest.main()
