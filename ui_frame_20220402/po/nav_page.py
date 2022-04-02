from common.file_reads import YamlRead
from setting import yaml_ele
from po.base_po import Base


class Nav(Base):
    Base.locators.update(YamlRead(yaml_ele['nav']).data_dic)

    def logout_action(self):
        # 点击注销
        self.logout.click()

    def ciustomer(self):
        # 点击查询
        self.vip.click()
