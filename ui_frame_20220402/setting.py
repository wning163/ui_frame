# ------------------webdriver驱动路径-------------
import os
PASH = os.path.dirname(__file__)  # 绝对路径
chrome_path = os.path.join(PASH, 'drivers/geckodriver.exe')
firefox_path = os.path.join(PASH, 'drivers/geckodriver.exe')
# ------------ locator_file 文件路径---------------
excel_info = {'path': os.path.join(PASH, 'data_info/test_data.xlsx'), 'sheet': 'test1'}

yaml_ele = {
    'login': os.path.join(PASH, 'po/locator/login_data.yaml'),
    'search': os.path.join(PASH, 'po/locator/search_data.yaml'),
    'nav': os.path.join(PASH, 'po/locator/nav_data.yaml'),
    'query': os.path.join(PASH, 'po/locator/query_data.yaml'),
}
# -------------------首页url-------------------------
home_page = 'http://192.172.2.234:8081/woniusales/'
# -------------------测试套件--------------------------
suite_module1 = ['test_login.py','test_logout.py']
suite_module2 = ['test_login.py','test_search.py','test_logout.py']
suite_module3 = ['test_login.py','test_query_all.py','test_logout.py']
suite_module4 = ['test_login.py','test_query_con.py','test_logout.py']




