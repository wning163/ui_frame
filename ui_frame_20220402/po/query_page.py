from time import sleep

from common.file_reads import YamlRead
from po.login_page import LoginPage
from setting import yaml_ele
from po.nav_page import Nav
from selenium.webdriver.support.select import Select


class Query(Nav):

    Nav.locators.update(YamlRead(yaml_ele['query']).data_dic)

    def query_all(self):
        self.zero_query.click()

    def query_con(self,goods='',g_name='',g_code='',g_type=''):
        self.query.click()

        self.goods.send_keys(goods)       # 货号
        self.goodsname.send_keys(g_name)  # 品名
        self.barcode.send_keys(g_code)    # 条码
        Select(self.goods_type).select_by_visible_text(g_type)  # 类型
        sleep(1)
        self.button_con.click()





if __name__ == '__main__':
    LoginPage().login()

    Query().query_con()