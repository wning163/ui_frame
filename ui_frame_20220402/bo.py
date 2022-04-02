import time
from typing import Type, Union
from selenium.webdriver import *
from setting import *


class Browser:

    IMP_TIME = 10  # 隐式等待超时
    PAGE_LOAD_TIME = 20  # 浏览器在执行脚本的过程中， 页面打开超时
    SCRIPTS_TIME = 20  # 浏览器，js脚本执行的超时
    HEADLESS = True   # 默认为调试模式。测试的时候会弹出框

    # 定义一个浏览器基类, 在基类中定义各个浏览器的驱动路径
    CHROME_DRIVER_PATH = chrome_path
    FIREFOX_DRIVER_PATH = firefox_path

    def __init__(self, driver_path: str = CHROME_DRIVER_PATH, browser_type: Type[Union[Chrome, Firefox, Ie]] = Chrome,
                 browser_options_type: Type[Union[ChromeOptions, FirefoxOptions, IeOptions]] = ChromeOptions):

        self.dirver_path = driver_path
        self.browser_type = browser_type  # 浏览器的类型
        self.browser_options_type = browser_options_type  # 浏览器启动项 CAP 类型

    @property
    def options(self):
        # 子类需要覆盖，用俩获取 浏览器的启动参数（specific  CAP）
        return

    @property
    def browser(self):
        # 子类需要覆盖，用来获取 对应浏览器的driver对象
        return


class Chrome(Browser):

    window_size = (1024, 728)         #  元组定义浏览器的窗口大小
    START_MAX = "--start-maximized"   #  启动项 ， 启动浏览器的最大话
    SCRIPTS_TIME = 30

    EXP = {
        "excludeSwitches": ['enable-automation', 'enable-logging'],
        "mobileEmulation": {'deviceName': 'Galaxy S5'}
    }

    HEADLESS = False

    @property
    def options(self):
        # 子类需要覆盖，用俩获取 浏览器的启动参数（specific  CAP）

        options = self.browser_options_type()  # 创建一个chrome浏览器的 option--- 》 ChromeOptions
        options.headless = self.HEADLESS       # 调试模式启动
        options.add_argument(self.START_MAX)
        for k, v in self.EXP.items():
            options.add_experimental_option(k, v)
        return options

    @property
    def browser(self):
        # 子类需要覆盖，用来获取 对应浏览器的driver对象

        browser= self.browser_type(executable_path=self.CHROME_DRIVER_PATH, options=self.options)
        browser.implicitly_wait(self.IMP_TIME)
        # browser.maximize_window
        browser.set_page_load_timeout(self.PAGE_LOAD_TIME)
        browser.set_script_timeout(self.SCRIPTS_TIME)
        return browser


class Firefox_browser(Browser):
    HEADLESS = False

    def __init__(self):
        super().__init__(driver_path=self.FIREFOX_DRIVER_PATH, browser_type=Firefox, browser_options_type=FirefoxOptions)

    @property
    def options(self):
        from selenium.webdriver.firefox.options import Options

        options = Options()
        options.headless = False
        return options

    @property
    def browser(self):
        driver = self.browser_type(options=self.options)
        return driver


if __name__ == '__main__':
    with Firefox_browser().browser as dr:
        dr.get('http://192.172.2.234:8081/woniusales/')
        time.sleep(3)

    # with Chrome().browser as bo:
    #     bo.get(url="http://www.baidu.com")
    #     time.sleep(3)


