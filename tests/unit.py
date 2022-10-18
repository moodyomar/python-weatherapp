import unittest
from utils import get_daily_data

class UnitTest(unittest.TestCase):
    def isApiCallTrue(self):
        self.assertIsNotNone(get_daily_data,"Api call return no values")