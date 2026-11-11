import re

phoneNumRegex1=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1=phoneNumRegex1.search('My phone is 223-313-4344')
print('Phone Number found:'+ mo1.group())
print(mo1.group(1))
print(mo1.groups())
areaCode,mainNumber = mo1.groups() 
print(areaCode)
print(mainNumber)

phoneNumRegex2=re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo2=phoneNumRegex2.search('My phone is (032) 429-4234')
print(mo2.group())
print(mo2.group(2))
print(mo2.groups())
