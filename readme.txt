* 使用unittest测试模块时候，发现import math,提示错误AttributeError:
module 'math' has no attribute 'createMath_add'。实际上是我生成的模块名
math.py与python自带的math模块重名了。import导入的顺序先自带模块，再程序文件夹。
所以一直发生错误。

*maths.py 模块改写def createMath_add(type, ab_max, cd_max)函数，使之能够指定被加数和加数
的范围，并检验相关逻辑。