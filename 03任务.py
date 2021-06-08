# a = input('输入数字1:')
# a = int(a)
# b = input("输入数字2：")
# b = int(b)
# c = input("输入数字3：")
# c = int(c)
# d = input("输入数字4：")
# d = int(d)
# e = input("输入数字5：")
# e = int(e)
# f = input("输入数字6：")
# f = int(f)
# g = input("输入数字7：")
# g = int(g)
# h = input("输入数字8：")
# h = int(h)
# i = input("输入数字9：")
# i = int(i)
# j = input("输入数字10：")
# j = int(j)
# t = a+b+c+d+e+f+g+h+i+j
# print (t)
# amax=max(a,b,c,d,e,f,g,h,i,j)
# print(amax)
# m = t/10
# print("最大值为:",m)

# import random
# num = random.randint(50,150)
# print(num)


a = input ("输入边长：")
a = int(a)
b=input ("输入边长：")
b = int(b)
c=input ("输入边长：")
c = int(c)
if a == b and a == c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等边三角形")
elif a == b and c > b and c > a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif a == b and  c < b and c < a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif a == c and b > a and b > c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif a == c and b < a and b < c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif b == c and a > b and a > c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif b == c and a < b and a < c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("等腰三角形")
elif a*a + b*b == c*c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("直角三角形")
elif a*a + c*c == b*b and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("直角三角形")
elif c*c + b*b == a*a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("直角三角形")
elif a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
    print("普通三角形")
else:
    print("不是三角形")

# A=56
# B=78
# C = A + B
# C = int(C)
# A = (C - A)
# B = (C - B)
# print("A=",A)
# print("B=",B)

# d = "root"
# f = "admin"
# c = 1
# a = input("请输入用户名：")
# while True :
#     print("第",c,"次输入")
#     b = input("请输入密码：")
#     c = c + 1
#     if c > 3 :
#         print("账户冻结")
#         break
#     if a == d and b == f :
#         print ("登陆成功")
#     elif  b !=f :
#         print("登录失败")


# name = "root"
# passward = "admin"
# count = 0
# while count < 3:
#     count = count + 1
#     name1 = input("请输入用户名：")
#     passward1 = input("请输入密码：")
#     if name1 == name and passward1 == passward:
#         print("登录成功！！")
#         break
#     elif name1 == name and count == 3 and passward1 != passward:
#         print("账户冻结！！")
#         break
#     else:
#         print("登录失败！")

# a = 0
# b = 0
# while b<101:
#     a = a + b
#     b = b + 1
#     c = a + b
#     print(int(c))


# a = 3
# b = 2
# c = 20
# d = (c-a)
# e = (a-b)
# f = d//e+1
# print("第",f,"天能够出来")


# a = ["北京","上海","广东","南京","杭州","福州","成都","哈尔滨","长春","沈阳","呼和浩特","石家庄","太原","济南","郑州","西安","兰州","银川","西宁","乌鲁木齐","合肥","长沙","南昌","武汉","成都","贵阳","海口","南宁","昆明"]
# a.append("重庆")
# print(a)
# a.insert(1,"广东")
# print(a)
# b=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# c=int(sum(b))
# d=int(c/8)
# print("前8城市GDP的总和为",c)
# print("前8城市的平均GDP为",d)

# a = [1,5,21,30,15,9,30,24]
# a.pop(0)
# a.pop(1)
# a.pop(3)
# a.pop(4)
# b=sum(a)
# print(b)


# a = [1,5,21,30,15,9,30,24]
# b = 0
# for i in a :
#     if i % 5 == 0 :
#      b = b + i
# print(b)




















































