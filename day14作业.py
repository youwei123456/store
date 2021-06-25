'''
    如何实现呢？
        python中提供实现多线程功能？
        1.子类继承threading.Thread子类
        2.重写run方法：写任务代码的
        3.调用start方法启动线程,自动执行run方法这里面任务代码
'''
import threading
import time

berad = 0

class  Chef(threading.Thread):
    __username = ""
    def setUsername(self,username):
       self.__username =username
    def getUsername(self,username):
        return self.__username
    def setCount(self,count):
        self.__count = count
    def getCount(self,count):
        return self.__count

    def run(self) -> None:
        global berad
        while True:
         if berad < 500 :
             self.__count = self.__count + 1
             time.sleep(0.1)
             print(self.__username,"做了一个面包","一共做了",self.__count,"个")

         elif berad == 500 :
             time.sleep(3)
         else:
             print(self.__username,"做了",self.__count,"个面包")
             break
         berad += 1

class People(threading.Thread):
    name = ""
    account = 0
    money = 1000
    def run(self) -> None:
        global berad
        global money
        while True :
            if berad > 0 :
                berad -= 1
                print(self.name, "购买了一个面包","还剩",berad,"个面包,余额为",self.money)
                if self.money == 0 :
                    print(self.name, "购买了", self.account, "个面包！")
                    break
            elif berad == 0 :
                time.sleep(2)
            self.money = self.money - 2
            self.account += 1
c1 = Chef()
c2 = Chef()
c3 = Chef()
c1.setUsername("张1")
c2.setUsername("王2")
c3.setUsername("李3")
c1.setCount(0)
c2.setCount(0)
c3.setCount(0)
p1 = People()
p2 = People()
p3 = People()
p4 = People()
p5 = People()
p1.name = "杨一"
p2.name = "杨二"
p3.name = "杨三"
p4.name = "杨4"
p5.name = "杨5"

c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

















