from pprint import pprint

import xlrd
import yaml
from os.path import exists
from setting import *


class ReadBase():

    def __init__(self, file_path):

        if not exists(file_path):
            print('——————————————警告：文件名不存在——————————')
        self.file_path = file_path
        self._data = None


class YamlRead(ReadBase):

    def __init__(self, file_path):
        super().__init__(file_path)

    @property
    def data_dic(self):
        with open(self.file_path, 'rb') as f:
            self._data = yaml.safe_load(f)

        return self._data


class ExeclRead(ReadBase):

    def __init__(self, file_path=excel_info['path'], sheet=excel_info['sheet']):
        super().__init__(file_path)
        self.sheet = sheet

    def data_dic(self,):
        my_book = xlrd.open_workbook(filename=self.file_path)
        sheet = my_book.sheet_by_name(self.sheet)

        r_num = sheet.nrows             # 行数
        title = sheet.row_values(0)   # 第一行数据
        self._date = []                # 存放信息列表套字典

        for i in range(1, r_num):      # 读取excl每行值
            x = zip(title, sheet.row_values(i))
            info = dict(x)


            self._date.append(info)
        return self._date


if __name__ == '__main__':
    pprint(ExeclRead(sheet='query').data_dic())
    pass


