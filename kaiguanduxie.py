#打开文件
f = open('a.txt','r')

#读取文件
result = f.read()
print(result)



#关闭文件
f.close()


#打开文件 open()
f = open('a.txt','w')

#写内容 write
f.write("hello java \n ")
f.write("hello php")

#关闭文件 close()
f.close()


#按⾏读取⽂件内容
# 打开
f = open('a.txt','r')
#按行读取
while True:
    line = f.readline()
    print(line,end='')
    if not line:
        break
#关闭文件 close()
f.close()

#读取所有的行 readlines()
