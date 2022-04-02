import time
import unittest
from po.search_page import SearchPage


class TestSearch(unittest.TestCase, SearchPage):

    def test_search(self):
        self.vip.click()          # 点击会员查询
        self.button_vip.click()   # 点击查询
        # 查询结过是否有第一行
        self.assertTrue(self.table_tr.is_displayed(),'无查询结果')


if __name__ == '__main__':
    unittest.main()
