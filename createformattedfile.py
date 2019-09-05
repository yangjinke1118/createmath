"""
本模块实现生成竖式、横式加减法；横式乘法
"""
from random import randint
from maths import createMath_add, createMath_dec, printMath_h, printMath_v
from operate_excel import OperateExcel

class CreateMathFile(OperateExcel):
    """
    本类继承自定义类OperateExcel（操作excel文件）
    实现多种类型数学计算练习文件生成功能
    """
    def __init__(self, path, modelfilename):
        super().__init__(path, modelfilename)
        self.sheet = self.wb.get_active_sheet()
        self.mathlist = []

        self.math0_pointdict = {  #  竖式坐标参数
            'op_row': 4,
            'op_column': 2,
            'a_row': 3,
            'a_column': 4,
            'b_row': 3,
            'b_column': 5,
            'c_row': 4,
            'c_column': 4,
            'd_row': 4,
            'd_column': 5,
            'e_row': 5,
            'e_column': 4,
            'f_row': 5,
            'f_column': 5,
            'row_offset': 3,
            'column_offset': 5,
        }
        self.math1_pointdict = {  # 横式坐标参数
            'op_row': 3,
            'op_column': 3,
            'ab_row': 3,
            'ab_column': 2,
            'cd_row': 3,
            'cd_column': 4,
            'ef_row': 3,
            'ef_column': 6,
            'row_offset': 1,
            'column_offset': 6,
        }

    def createOneUnit_v(self, types, i, j):
        """
        根据type类型，生成一个单元的竖式计算式子
        :param mathlist: 传入的计算式子因子
        :param types: 生成计算练习类型。
        types=0,竖式加法
        types=1,竖式减法
        types=2,竖式加减混合
        types=3,竖式加法逆向思维
        types=4,竖式减法逆向思维
        :param i,j:传入模版当前生成单元坐标
        :return:
        """
        op = self.mathlist[0]
        a = self.mathlist[1]
        b = self.mathlist[2]
        c = self.mathlist[3]
        d = self.mathlist[4]
        e = self.mathlist[5]
        f = self.mathlist[6]

        row_offset = self.math0_pointdict['row_offset']
        column_offset = self.math0_pointdict['column_offset']
        op_row = self.math0_pointdict['op_row'] + row_offset * i
        op_column = self.math0_pointdict['op_column'] + column_offset * j
        a_row = self.math0_pointdict['a_row'] + row_offset * i
        a_column = self.math0_pointdict['a_column'] + column_offset * j
        b_row = self.math0_pointdict['b_row'] + row_offset * i
        b_column = self.math0_pointdict['b_column'] + column_offset * j
        c_row = self.math0_pointdict['c_row'] + row_offset * i
        c_column = self.math0_pointdict['c_column'] + column_offset * j
        d_row = self.math0_pointdict['d_row'] + row_offset * i
        d_column = self.math0_pointdict['d_column'] + column_offset * j
        e_row = self.math0_pointdict['e_row'] + row_offset * i
        e_column = self.math0_pointdict['e_column'] + column_offset * j
        f_row = self.math0_pointdict['f_row'] + row_offset * i
        f_column = self.math0_pointdict['f_column'] + column_offset * j

        if (types >= 0) and (types <= 2):
            self.sheet.cell(row=op_row, column=op_column).value = op
            if a == 0:
                self.sheet.cell(row=a_row, column=a_column).value = ''
                self.sheet.cell(row=b_row, column=b_column).value = b
            else:
                self.sheet.cell(row=a_row, column=a_column).value = a
                self.sheet.cell(row=b_row, column=b_column).value = b
            if c == 0:
                self.sheet.cell(row=c_row, column=c_column).value = ''
                self.sheet.cell(row=d_row, column=d_column).value = d
            else:
                self.sheet.cell(row=c_row, column=c_column).value = c
                self.sheet.cell(row=d_row, column=d_column).value = d
        elif types == 3 or types == 4 or types == 5:
            self.sheet.cell(row=op_row, column=op_column).value = op
            i = randint(0, 1)
            if i == 0:
                if a == 0:
                    self.sheet.cell(row=a_row, column=a_column).value = ''
                    self.sheet.cell(row=b_row, column=b_column).value = b
                else:
                    self.sheet.cell(row=a_row, column=a_column).value = a
                    self.sheet.cell(row=b_row, column=b_column).value = b
                self.sheet.cell(row=c_row, column=c_column).value = '□'
                self.sheet.cell(row=d_row, column=d_column).value = '□'
                self.sheet.cell(row=e_row, column=e_column).value = e
                self.sheet.cell(row=f_row, column=f_column).value = f
            elif i == 1:
                self.sheet.cell(row=a_row, column=a_column).value = '□'
                self.sheet.cell(row=b_row, column=b_column).value = '□'
                if c == 0:
                    self.sheet.cell(row=c_row, column=c_column).value = ''
                    self.sheet.cell(row=d_row, column=d_column).value = d
                else:
                    self.sheet.cell(row=c_row, column=c_column).value = c
                    self.sheet.cell(row=d_row, column=d_column).value = d
                self.sheet.cell(row=e_row, column=e_column).value = e
                self.sheet.cell(row=f_row, column=f_column).value = f

    def createMathFile_v(self, types, level, path, filename):
        """
        根据type类型生成竖式计算练习文件
        :param types: =0,竖式加法；=1，竖式减法；=2，竖式加减混合法；
            =3,竖式加法逆向思维；=4,竖式减法逆向思维；
        :param level: =0，不强制进位、退位，=1，强制进位、退位。
        :param path:生成文档路径
        :param filename:生成文档名
        :return:
        """
        for i in range(0, 9):
            for j in range(0, 4):
                if types == 0 or types == 3:
                    self.mathlist = createMath_add(level)
                elif types == 1 or types == 4:
                    self.mathlist = createMath_dec(level)
                elif types == 2 or types == 5:
                    if randint(0, 1) == 0:
                        self.mathlist = createMath_dec(level)
                    else:
                        self.mathlist = createMath_add(level)
                self.createOneUnit_v(types, i, j)
                printMath_v(self.mathlist)
        self.save_as(path, filename)

    def createOneUnit_h(self, types, i, j):
        """
        根据type类型，生成一个单元的横计算式子
        :param mathlist: 传入的计算式子因子
        :param types: 生成计算练习类型。
        types=0,横式加法
        types=1,横式减法
        types=2,横式加减混合
        types=3,横式加法逆向思维
        types=4,横式减法逆向思维
        :param i,j:传入模版当前生成单元坐标
        :return:
        """
        op = self.mathlist[0]
        a = self.mathlist[1]
        b = self.mathlist[2]
        c = self.mathlist[3]
        d = self.mathlist[4]
        e = self.mathlist[5]
        f = self.mathlist[6]

        if a == 0:
            ab = str(b)
        else:
            ab = str(a) + str(b)
        if c == 0:
            cd = str(d)
        else:
            cd = str(c) + str(d)
        if e == 0:
            ef = str(f)
        else:
            ef = str(e) + str(f)

        row_offset = self.math1_pointdict['row_offset']
        column_offset = self.math1_pointdict['column_offset']
        op_row = self.math1_pointdict['op_row'] + row_offset * i
        op_column = self.math1_pointdict['op_column'] + column_offset * j
        ab_row = self.math1_pointdict['ab_row'] + row_offset * i
        ab_column = self.math1_pointdict['ab_column'] + column_offset * j
        cd_row = self.math1_pointdict['cd_row'] + row_offset * i
        cd_column = self.math1_pointdict['cd_column'] + column_offset * j
        ef_row = self.math1_pointdict['ef_row'] + row_offset * i
        ef_column = self.math1_pointdict['ef_column'] + column_offset * j

        if (types >= 0) and (types <= 2):
            self.sheet.cell(row=op_row, column=op_column).value = op

            self.sheet.cell(row=ab_row, column=ab_column).value = ab

            self.sheet.cell(row=cd_row, column=cd_column).value = cd

            self.sheet.cell(row=ef_row, column=ef_column).value = ''
        elif types == 3 or types == 4 or types == 5:
            self.sheet.cell(row=op_row, column=op_column).value = op
            i = randint(0, 1)
            if i == 0:
                self.sheet.cell(row=ab_row, column=ab_column).value = ab

                self.sheet.cell(row=cd_row, column=cd_column).value = '□'

                self.sheet.cell(row=ef_row, column=ef_column).value = ef
            elif i == 1:
                self.sheet.cell(row=ab_row, column=ab_column).value = '□'

                self.sheet.cell(row=cd_row, column=cd_column).value = cd

                self.sheet.cell(row=ef_row, column=ef_column).value = ef

    def createMathFile_h(self, types, level, path, filename):
        """
        根据type类型生成横式计算练习文件
        :param types: =0,横式加法；=1，横式减法；=2，横式加减混合法；
            =3,横式加法逆向思维；=4,横式减法逆向思维；
        :param level: =0，不强制进位、退位，=1，强制进位、退位。
        :param path:生成文档路径
        :param filename:生成文档名
        :return:
        """
        for i in range(0, 26):
            for j in range(0, 3):
                if types == 0 or types == 3:
                    self.mathlist = createMath_add(level)
                elif types == 1 or types == 4:
                    self.mathlist = createMath_dec(level)
                elif types == 2 or types == 5:
                    if randint(0, 1) == 0:
                        self.mathlist = createMath_dec(level)
                    else:
                        self.mathlist = createMath_add(level)
                self.createOneUnit_h(types, i, j)
                printMath_h(self.mathlist)
        self.save_as(path, filename)
