
import unittest

import pyted

class TestMethods(unittest.TestCase):
    def setUp(self):
        pass 
    
    def test_add(self):
        self.assertEqual(pyted.smile(), ":)")
    def test_add_second(self):
        self.assertEqual(pyted.frown(), ":(")
    def test_version(self):
        self.assertEqual(pyted.__version__, "")
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
