import unittest
from setting import *


if __name__ == '__main__':
    suite = unittest.TestSuite()

    for test_suite in suite_module4:
        print(test_suite)
        discover = unittest.defaultTestLoader.discover(start_dir='tests',pattern=test_suite)
        suite.addTests(discover)

    from common.HTMLTestRunner import HTMLTestRunner
    with open('./report.html','wb') as f:
        runner = HTMLTestRunner(f, verbosity=2)
        runner.run(suite)



