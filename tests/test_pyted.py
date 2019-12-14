import unittest

import pyted

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(pyted.smile(), ":)")
        def test_add_second(self):
            self.assertEqual(pyted.frown(), ":(")
if __name__ == '__main__':
    unittest.main()
