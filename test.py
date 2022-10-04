import unittest
from utils import is_url_up

class LocalTest(unittest.TestCase):

    def testConnectionOk(self):
        self.assertTrue(is_url_up("http://localhost:3000"),'Website is Not Up!')

        
        
    
     