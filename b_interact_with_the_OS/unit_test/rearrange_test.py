import unittest
from rearrange import rearrange_name

print(rearrange_name('loera, mario'))

class TestRearrenge(unittest.TestCase):
    def test_basic(self):
        testcase = 'loera, mario'
        expected = 'mario loera'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_doble_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = 'Mario'
        expected = 'Mario'
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_multi(self):
        data = [['loera, mario', 'mario loera'],
                ['Hopper, Grace M.','Grace M. Hopper'],
                ['loera', 'loera']]
        for d in data:
            self.assertEqual(rearrange_name(d[0]), d[1])

unittest.main()