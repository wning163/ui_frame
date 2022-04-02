from setting import yaml_ele
from common.file_reads import YamlRead
from po.nav_page import Nav


class LoginPage(Nav):

    Nav.locators.update(YamlRead(yaml_ele['login']).data_dic)

    def login(self,name='admin',pwd='123',verif='0000'):

        # 登陆
        self.driver.get(self.url)
        self.username.send_keys(name)
        self.password.send_keys(pwd)
        self.verifcode.send_keys(verif)
        self.button.click()


if __name__ == '__main__':
    LoginPage().login()
