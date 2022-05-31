astr = "world"
if astr.startswith('o'):
  print('ture')
else:
    print('false')

bstr = "1234"
if bstr.isdigit():
    print('ture')
else:
    print('false')

cstr = "asdfgh"
if cstr.isalpha():
    print('ture')
else:
    print('false')

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
fstr = "asdfgh678 %^&*"
zm = 0
kg = 0
sz = 0
other = 0
for x in fstr:
    if x.isalpha(): #判断是字母
        zm += 1
    elif x.isdigit(): #判断是数字
        sz += 1
    elif x.isspace(): #判断是空格
        kg += 1
    else:
        other += 1
print("字母的个数为：",zm)
print("数字的个数为：",kg)
print("空格的个数为：",sz)
print("字符的个数为：",other)




