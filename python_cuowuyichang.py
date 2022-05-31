def div1(x,y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("不能被0整除")
       # print(e)

print(div1(3,4))
print(div1(3,0))
print(div1(6,6))