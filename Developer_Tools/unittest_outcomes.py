# unittest_outcomes.py

import unittest

class OutcomesTest(unittest.TestCase):
    def testPass(self):
        pass
    def testFail(self):
        self.assertFalse(True)
    def testError(self):
        raise RuntimeError('Test error!')
