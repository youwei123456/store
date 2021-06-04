import random
num = random.randint(0,1000)
i = 0
b = 5000
c = 0
while i < 10 and c < 15 :
    print("第",i,"次！")
    print("还剩",b,"金币！")
    a = input("请输入你所想的数：")
    a = int(a)
    if a > num:
        b = b-500
        print("大了，听明白了没有!!!")
    elif a < num:
        b = b - 500
        print("猜的什么玩意儿？小了！！！")
    elif b < 500:
        print("游戏结束")
    else:
        b = b + 3000
        print("hui物，终于猜对了！！！")
        break
    i = i+1
    c = c+1

