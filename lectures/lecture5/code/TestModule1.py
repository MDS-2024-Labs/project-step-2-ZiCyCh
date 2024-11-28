import unittest
from mod1 import addition as md1
from mod2 import subtraction as md2

class TestAdd(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(md1(1,1),2)
        self.assertEqual(md1(1,2),3)
     
