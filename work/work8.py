# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 1
b = 2
c = 3
d = 4
print(a+b-c*d)
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for a in range(1,101):
  if a % 3 == 0:
      sum += a
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for  a in range(1,11,2):
    print(a)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for a in range(1,101):
    if a % 2 == 0:
        sum1 +=a
    else:
        sum2 +=a
print(sum1-sum2)
# 5. 求1+2+3+...+100的和
sum = 0
for a in range(1,101):
    sum += a
print(sum)

# 6. 判断一个数n能同时被3和5整除
a = input("请输入一个整数:")
if int(a)% 3==0 and int(a)%5 == 0:
    print(a,"能被3和5整除")
else:
    print(a,"不能被3和5整除")
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = input("请输入一个整数:")
if 1< int(a)< 100:
 print("a是1-100内的数")
else:
 print("a不是1-100内的数")
# #8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
lst=[]
a = input("请输入一个整数:")
b = input("请输入一个整数:")
c = input("请输入一个整数:")
lst.append(a)
lst.append(b)
lst.append(c)
print(lst)
lst.sort()
print(lst)


