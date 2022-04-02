import time
import unittest
from po.query_page import Query


class TestSearchAll(unittest.TestCase,Query):

    def test_query_all(self):
        self.query.click()  # 点击库存查询
        self.zero_query.click()  # 点击零库存查询
        # 查询结过是否有第一行
        self.assertTrue(self.query_result.is_displayed(),'无查询结果')


if __name__ == '__main__':
    unittest.main()
