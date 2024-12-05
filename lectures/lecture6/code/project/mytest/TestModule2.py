import unittest
from mypackage.subpkg1.mod1 import addition as md1
from mypackage.subpkg2.mod2 import subtraction as md2

class TestSub(unittest.TestCase):
    
    def test_subtraction(self):
        self.assertEqual(md2(1,1),1)
        self.assertEqual(md2(1,2),-1)