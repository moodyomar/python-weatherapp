import unittest
from utils import get_daily_data

class UnitTest(unittest.TestCase):
    def testApiCall(self):
        self.assertIsNotNone(get_daily_data(),"Api call return no values")

   
if __name__ == '__main__':
   unittest.main()