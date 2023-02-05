import requests  # 这个请求模块是我原先设想的这款软件的真正用途
import time  # 先定义一个时间控制模块，后面登录太快有那么亿点点不合实际

print("hello,nice to meet you")
print("感谢您选择此产品!\n")  # 就是一些废话
time.sleep(3)  # 让这个程序运行的慢一些

name = input("please choose your name：\n")  # 写上你该死欸的昵称
password = input("please setting your password:\n")  # 设置一下你该死的密码

print("sign successfully!!!\n")  # 这是废话
print("these are your account profession,please save it\n")  # 记住你该死的账户信息，别他妈两分钟再忘了冲我要密码
print("this is your name:", name)  # 这他妈是你名字
print("this your password:", password)  # 这他妈是你密码
time.sleep(4)  # 再让它运行慢一点
print("next,let us to use it\n")  # 这也是废话
print("if you want it be work,that you should give it a signal\n")  # 这也是废话
print("please wait......")  # 这是废话
time.sleep(10)  # 再让它运行慢一点

c = requests.get('')#就各这儿，怕你眼瞎，手动填上你网址
print(c.text)  # tmlgb自己看看你自己搜哩啥吊玩意儿



