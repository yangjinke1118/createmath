import os
from createformattedfile import CreateMathFile

cwd = os.getcwd()
my_create = CreateMathFile(cwd, '竖式算术生成模版.xlsx')
my_create1 = CreateMathFile(cwd, '横式算术生成模版.xlsx')
new_path = os.path.join(cwd, 'files')
new_filename = 'math'

# 查看files文件夹下是否有math?.xlsx文档，如果有则删除
for filename in os.listdir('files'):
    if filename.startswith('math') and filename.endswith('.xlsx'):
        os.unlink('.\\files\\' + filename)

for i in range(0, 4):
    """
    :types: =0,竖式加法；=1，竖式减法；=2，竖式加减混合法；
            =3,竖式加法逆向思维；=4,竖式减法逆向思维；
    :level: =0，不强制进位、退位，=1，强制进位、退位。
    """
    my_create.createMathFile_v(2, 1, new_path, new_filename + '_v' + str(i) + '.xlsx')

for i in range(0, 4):
    """
    :types: =0,竖式加法；=1，竖式减法；=2，竖式加减混合法；
            =3,竖式加法逆向思维；=4,竖式减法逆向思维；
    :level: =0，不强制进位、退位，=1，强制进位、退位。
    """
    my_create1.createMathFile_h(2, 1, new_path, new_filename + '_h' + str(i) + '.xlsx')

