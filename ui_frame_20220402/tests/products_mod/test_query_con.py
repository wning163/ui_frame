import time
import unittest
from ddt import ddt,unpack,data
from common.file_reads import ExeclRead, excel_info
from po.query_page import Query

@ddt
class TestSearchCon(unittest.TestCase,Query):

    info = ExeclRead(file_path=excel_info['path'], sheet='query').data_dic()

    @unpack
    @data(*info)
    def test_query_con(self,goods,g_name,g_code,g_type):

        time.sleep(1)
        self.query_con(goods,g_name,g_code,g_type)  # 点击条件查询
        # 查询结过是否有第一行
        self.assertTrue(self.query_result.is_displayed(),'无查询结果')
        time.sleep(1)

        self.query.click()

        # LoginPage().logout_action()


if __name__ == '__main__':
    TestSearchCon().query_con()

