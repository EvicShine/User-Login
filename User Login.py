"""
制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：
登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。
提示：系统先验证验证码是否正确，正确后再验证用户名和密码。
"""
"方法一:"
"""
# 定义三个变量,并赋值
username = 'aaa'
password = '123456'
code1 = 'qwer'

# 执行登录代码操作
a = input('请输入验证码:')
if a == code1:
    b = input('请输入用户名:')
    if b == username:
        c = str(input('请输入密码:'))
        if c == password:
            print('登录成功!')
        else:
            print('密码错误,请重新登录!')
    else:
        print('用户名错误,请重新登录')
else:
    print('验证码错误,60s后再试!')
"""
"方法二:"
# 定义三个变量,并赋值
username = 'aaa'
password = '123456'
code1 = 'qwer'

# 接收用户输入的数据
a = input('请输入验证码:')
b = input('请输入用户名:')
c = input('请输入密码:')

# 执行登录功能
if a == code1:
    print('验证码正确,', end='')     # 实现语句连续,不换行
    if b == username and c == password:
        print('登录成功!')
    else:
        print('用户名或密码错误!')
else:
    print('验证码错误!')
