import time

from setting import yaml_ele
from common.file_reads import YamlRead
from po.nav_page import Nav


class SearchPage(Nav):

    Nav.locators.update(YamlRead(yaml_ele['search']).data_dic)

    def search_all(self):
        # 点击查询
        self.button_vip.click()


if __name__ == '__main__':
    SearchPage().search_all()
    time.sleep(3)

