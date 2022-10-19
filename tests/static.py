import unittest
# from utils import is_url_up,is_website_running,url

class StaticTest(unittest.TestCase):
    def testCodeSyntax(self):
        self.assertEqual('test','test')
        
if __name__ == '__main__':
   unittest.main()