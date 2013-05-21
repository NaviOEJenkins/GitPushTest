def test_b():
    assert 'b' == 'b'

class TestExampleTwo:
    def test_c(self):
        assert 'c' == 'c'

import unittest

class ExampleTest(unittest.TestCase):
    def test_a(self):
        self.assert_(1 == 1)

"""
def test_evans():
    for i in range (0, 5):
        yield check_even, i, i*3

def check_even(n, nn):
    assert n % 2 == 0 or nn % 2 == 0
"""

