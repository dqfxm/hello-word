#del0506计算连续质数之和，测试dell同步git第二次测试
#工作仓库为hello-word
#再次测试退送到其他仓库,这是一个新分支
def prime(m):
    result = ""  #返回的结果
    i = 0 #用来记录次数
    start = int(m)+1
    while i<5:  
        for j in range(2,start):
            if start%j == 0:
                break
        else:
            result =result+str(start)+','
            i+=1
        start += 1
    return result
n = eval(input("请输入一个整数:"))
m = prime(n)
print(m[:-1])