
#找到列表最大值

s=[]
j=0
while True: 
    
    print('Enter the number ' + str(len(s) + 1) + 
      ' (Or enter nothing to stop.):') 
    number =input() 
    if number == '': 
        break 
    s.append(int(number))

print(s)
max_s=s[0]
for i in range(len(s)):
    if max_s<s[i]:
        max_s=s[i]
print(max_s)