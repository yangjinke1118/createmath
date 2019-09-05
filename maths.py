"""
本模块实现各种数学算术题型
1、竖式100以内加减法，进位、借位；逆向思维
2、横式100以内加减法，进位、借位，逆向思维
3、个位乘法，十位数除法。
"""
from random import randint

def createMath_add(type):
    """
    100以内加法生成，返回加数，被加数，结果的十位、个位 数字
    type = 0：普通生成方式
    type = 1：特殊生成方式，个位必须有进位
    """
    b = randint(0, 9)
    d = randint(0, 9)
    if type == 1:
        while b+d < 10:
            b = randint(0, 9)
            d = randint(0, 9)
    if b + d >= 10:
        a = randint(0, 9)
        c = randint(0, 9)
        while a+c >= 9:
            a = randint(0, 9)
            c = randint(0, 9)
    else:
        a = randint(0, 9)
        c = randint(0, 9)
        while a + c > 9:
            a = randint(0, 9)
            c = randint(0, 9)
    math_result = a * 10 + b + c * 10 + d
    e = math_result // 10
    f = math_result % 10

    return ['+', a, b, c, d, e, f]

def createMath_dec(type):
    """
    100以内减法生成，返回减数，被减数，结果的十位、个位 数字
    type = 0：普通生成方式
    type = 1：特殊生成方式，十位必须有退位
    """
    b = randint(0, 9)
    d = randint(0, 9)
    if type == 1:  # 有退位
        while b >= d:  # b < d 才退出循环
            b = randint(0, 9)
            d = randint(0, 9)
    if b >= d:
        a = randint(0, 9)
        c = randint(0, 9)
        while a < c:
            a = randint(0, 9)
            c = randint(0, 9)
    else:
        a = randint(0, 9)
        c = randint(0, 9)
        while a <= c:
            a = randint(0, 9)
            c = randint(0, 9)
    math_result = a * 10 + b - c * 10 - d
    e = math_result // 10
    f = math_result % 10
    return ['-', a, b, c, d, e, f]

def createMath_Mul():
    """
    生成十以内的乘法
    :return: 以列表形式，返回乘数，被乘数，结果 十位，个位数
    """
    a = 0
    b = randint(0, 9)
    c = 0
    d = randint(0, 9)
    result = b * d
    e = result // 10
    f = result % 10
    return ['×', a, b, c, d, e, f]

def createMath_div():
    """
    生成被除数100以内，除数10以内的除法
    :return: 以列表形式，返回除数，被数，结果 十位，个位数
    """
    c = 0
    while True:
        a = randint(0, 9)
        b = randint(0, 9)
        d = randint(0, 9)
        if d == 0:
            continue
        if (a * 10 + b) % d == 0:
            break

    result = (a * 10 + b) / d
    e = result // 10
    f = result % 10
    return ['÷', a, b, c, d, e, f]



def printMath_v(mathlist):
    if str(type(mathlist)) != "<class 'list'>":
        print('Error:Please Enter a list object!')
        return
    if len(mathlist) != 7:
        print('Error:The list has not 5 elements!')
        return
    op = mathlist[0]
    a = mathlist[1]
    b = mathlist[2]
    c = mathlist[3]
    d = mathlist[4]
    e = mathlist[5]
    f = mathlist[6]
    print('    ' + str(a) + '  ' + str(b))
    print(op + '   ' + str(c) + '  ' + str(d))
    print('----------')
    print('    ' + str(e) + '  ' + str(f))
    print('')

def printMath_h(mathlist):
    if str(type(mathlist)) != "<class 'list'>":
        print('Error:Please Enter a list object!')
        return
    if len(mathlist) != 7:
        print('Error:The list has not 5 elements!')
        return
    op = mathlist[0]
    a = mathlist[1]
    b = mathlist[2]
    c = mathlist[3]
    d = mathlist[4]
    e = mathlist[5]
    f = mathlist[6]
    print('  ' + str(a) + str(b) + ' ' + op + ' ' + str(c) + str(d) + ' = ' + str(e) + str(f))
    print('')

def runMath(mathlist):
    if str(type(mathlist)) != "<class 'list'>":
        print('Error:Please Enter a list object!')
        return
    if len(mathlist) != 7:
        print('Error:The list has not 5 elements!')
        return
    op = mathlist[0]
    a = mathlist[1]
    b = mathlist[2]
    c = mathlist[3]
    d = mathlist[4]
    firstNum = a*10 + b
    secondNum = c*10 + d
    if op == '+':
        print(str(firstNum + secondNum))
    elif op == '-':
        print(str(firstNum - secondNum))

