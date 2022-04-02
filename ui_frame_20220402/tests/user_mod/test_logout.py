import time
import unittest
from po.nav_page import Nav



class TestLogin(unittest.TestCase, Nav):

    def test_logout(self):
        self.logout_action()



if __name__ == '__main__':
    unittest.main()