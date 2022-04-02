from bo import Firefox_browser
from setting import home_page
class Base():

    url = home_page
    driver = Firefox_browser().browser
    locators = {}

    def __getattr__(self,msg):
        #  如果msg在locators中，就找到元素
        if msg in self.locators:
            msg_value = self.locators[msg]
            return self.driver.find_element(*msg_value)

        else:
            return None