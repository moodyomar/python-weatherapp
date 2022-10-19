import unittest
# from utils import get_daily_data
from utils import is_url_up,url

class UnitTest(unittest.TestCase):
    # def testApiCall(self):
    #     self.assertIsNotNone(get_daily_data(),"Api call return no values")
      
    def testConnectionOk(self):
        self.assertTrue(is_url_up(url),'Website is Not Up!')  
        
if __name__ == '__main__':
   unittest.main()