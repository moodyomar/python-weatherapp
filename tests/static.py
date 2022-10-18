import unittest
# from utils import is_url_up,is_website_running,url

class StaticTest(unittest.TestCase):
    def isCodeOK(self):
        self.assertEqual('test','test')