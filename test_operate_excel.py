import unittest, os
from openpyxl import worksheet
from operate_excel import OperateExcel

class TestOperateExcel(unittest.TestCase):

    def setUp(self):
        self.path = os.getcwd()
        self.name = '竖式算术生成模版.xlsx'
        self.op_excel = OperateExcel(self.path, self.name)
        self.op_excel.get_active_sheet()
        self.cell_index = [1, 1]
        self.cell_value = 'test'
        self.datas = [1, 2, 'hello world']


    def test_workbook_object(self):
        sheet_title = self.op_excel.sheet.title
        self.assertEqual(sheet_title, 'Sheet1')

    def test_enter_data_cell_and_get_data_from_cell(self):
        self.op_excel.sheet.cell(row=self.cell_index[0], column=self.cell_index[1]).value = \
            self.cell_value
        self.assertEqual(self.cell_value, self.op_excel.get_cell_data(self.cell_index[0],
                                                                      self.cell_index[1]))

    def test_enter_datas_row_and_get_datas_from_row(self):
        self.op_excel.enter_datas_to_row(self.cell_index, self.datas)
        self.assertEqual(self.datas, self.op_excel.get_row_datas(self.cell_index, 3))


unittest.main
