"""
本模块实现各种数学算术题型
1、竖式100以内加减法，进位、借位；逆向思维
2、横式100以内加减法，进位、借位，逆向思维
3、个位乘法，十位数除法。
"""
from random import randint

def get_ab_cd(ab_max, cd_max):
    ab = 0
    cd = 0
    # 获取符合要求的ab数值
    if ab_max > 9 and ab_max <= 99:  # 当ab最大值大于9
        ab = randint(0, ab_max)
        while ab <= 9:
            ab = randint(0, ab_max)  # 直到获取符合条件的ab数值,10-99
    elif ab_max > 99 and ab_max <= 999:
        ab = randint(0, ab_max)
        while ab <= 99:
            ab = randint(0, ab_max)  # 直到获取符合条件的ab数值,100-999
    elif ab_max <= 9:
        ab = randint(0, ab_max)
        while ab > 9:
            ab = randint(0, ab_max)  # 直到获取符合条件的ab数值,0-9

        # 获取符合要求的cd数值
    if cd_max > 9 and cd_max <= 99:  # 当ab最大值大于9
        cd = randint(0, cd_max)
        while cd <= 9:
            cd = randint(0, cd_max)  # 直到获取符合条件的cd数值,10-99
    elif cd_max > 99 and cd_max <= 999:
        cd = randint(0, cd_max)
        while cd <= 99:
            cd = randint(0, cd_max)  # 直到获取符合条件的cd数值,100-999
    elif cd_max <= 9:
        cd = randint(0, cd_max)
        while cd > 9:
            cd = randint(0, cd_max)  # 直到获取符合条件的cd数值,0-9
    return ab, cd


def createMath_add(type, ab_max, cd_max):
    """
    100以内加法生成，返回加数，被加数，结果的十位、个位 数字
    type = 0：普通生成方式
    type = 1：特殊生成方式，个位必须有进位
    ab_max表示被加数最大值上限，如果大于10，则ab不会小于10
    cd_max表示加数最大值上限。
    """
    if ab_max >= 100 or cd_max >= 100:
        return -1

    ab, cd = get_ab_cd(ab_max, cd_max)
    if type == 0:  # 不进位
        while int(str(ab)[-1]) + int(str(cd)[-1]) > 9:
            ab, cd = get_ab_cd(ab_max, cd_max)
    elif type == 1:  # 进位
        while int(str(ab)[-1]) + int(str(cd)[-1]) < 9:
            ab, cd = get_ab_cd(ab_max, cd_max)



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

