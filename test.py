import unittest
from utils import is_url_up,is_website_running

class LocalTest(unittest.TestCase):

    def testConnectionOk(self):
        self.assertTrue(is_url_up("http://localhost:3000"),'Website is Not Up!')
        
    def testWebsiteRunning(self):
        self.assertEqual(is_website_running("http://localhost:3000"),'Weather Web App v2')
        
        
    
     