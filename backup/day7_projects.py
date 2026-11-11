# import pyperclip
# pyperclip.copy('''大家好，我是张三（zhangsan_2024@qq.com），
# 如果遇到系统问题，请联系客服（support_team@163.com），
# 或者直接发邮件给老板（boss@gmail.com）。''')
# pyperclip.paste()
# print(pyperclip.paste())


import re
# import pyperclip  # 等代码跑通了，再把这个加上去读取剪贴板

text = """
大家好，有事请联系：
张三：138-1234-5678
李四：(032) 429-4234
王五：139.8888.9999 ext. 123
客服邮箱：support_team@163.com
老板邮箱：boss_2024@gmail.com,备用邮箱 admin@company.com.cn
"""
# 1. 邮箱正则（稍微升级了一下，支持带点、下划线、减号）
email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
emails = email_regex.findall(text)
# 2. 电话正则（支持 区号、空格、横杠、点号、分机号）
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # 区号：3个数字 或 带括号的3个数字（可选）
    (\s|-|\.)?                  # 分隔符：空格、横杠、或点号（可选）
    (\d{3,4})                   # 前三位：改成 3 到 4 个数字
    (\s|-|\.)                   # 分隔符
    (\d{4,})                    # 后四位：改成 4 个及以上数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # 分机号（可选）
    )''', re.VERBOSE)
phones = phone_regex.findall(text)
# 3. 整理结果
matches = []

# 处理邮箱（邮箱直接是字符串列表，直接加进去就行）
for email in emails:
    matches.append(email)

# 处理电话（电话是元组，我们需要拼装一下）S
for phone_tuple in phones:
    phone_str = phone_tuple[0].replace(' ', '-').replace('.', '-')
    phone_str = re.sub(r'-+', '-', phone_str) # 把连续的 - 变成一个
    if phone_str not in matches:
        matches.append(phone_str)

# 4. 打印最终结果
print("=== 提取结果 ===")
if len(matches) > 0:
    for item in matches:
        print(item)
else:
    print("没有找到任何电话号码或邮箱。")

import re

def check_password(password):
    # 1. 编译四个正则表达式
    len_regex = re.compile(r'.{8,}')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    
    # 2. 用 search 挨个测试，只要有任何一个返回 None，就说明不合格
    if len_regex.search(password) == None:
        return "密码太短,至少需要8个字符!"
    if upper_regex.search(password) == None:
        return "密码必须包含至少一个大写字母！"
    # 继续写小写和数字的判断...
    if lower_regex.search(password) == None:
        return "密码必须包含至少一个小写字母！"
    if digit_regex.search(password) == None:
        return "密码必须包含至少一个数字！"
    
    return "密码强度合格！"

# 测试
print(check_password("abc"))  # 太短
print(check_password("abcdefgh"))  # 没大写、没数字
print(check_password("Abcdefg1"))  # 强口令！
password = input("请输入密码进行验证：")
result = check_password(password)
print(result)