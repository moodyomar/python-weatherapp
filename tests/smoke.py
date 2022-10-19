import unittest
from utils import is_url_up,is_website_running,url

class LocalTest(unittest.TestCase):

    def testConnectionOk(self):
        self.assertTrue(is_url_up(url),'Website is Not Up!')
        
    def testWebsiteRunning(self):
        self.assertEqual(is_website_running(url),'Weather Web App v2')

if __name__ == '__main__':
   unittest.main()