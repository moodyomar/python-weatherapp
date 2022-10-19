import unittest


class StaticTest(unittest.TestCase):
    def testCodeSyntax(self):
        self.assertEqual('test','test')