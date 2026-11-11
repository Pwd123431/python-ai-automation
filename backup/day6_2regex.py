import re

phoneNum=re.compile(r'\((\d{3})\) (\d{3}-\d{4})')
mo1=phoneNum.search("My phone is (323) 311-4442 and (312) 313-3311")
print("phone number is "+ mo1.group())

str=phoneNum.findall("My phone is (323) 311-4442 and (312) 313-3311")
print("phone number is ",str)


text = """
大家好，我是张三（zhangsan_2024@qq.com），
如果遇到系统问题，请联系客服（support_team@163.com），
或者直接发邮件给老板（boss@gmail.com）。
"""

email=re.compile(r'''\w+@\w+\.\w+''')
emails=email.findall(text)
print("提取的邮箱：",emails)