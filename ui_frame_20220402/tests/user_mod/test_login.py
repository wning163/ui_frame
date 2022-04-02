import time
import unittest
from po.login_page import LoginPage


class TestLogin(unittest.TestCase, LoginPage):

    def test_login(self):
        self.driver.get(self.url)
        self.login()
        # 注销按钮
        self.assertTrue(self.logout.is_displayed(),'登陆不成功')


if __name__ == '__main__':
    unittest.main()