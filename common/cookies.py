#作者所属：尹乐
## 获取登录缓存cookies
import json

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from data import get_local

class LoginCookies():

    def __init__(self,driver): #实例化
        self.driver=driver

    def get_cookies(self):         #此函数留做模模板 ，获取cookies  直接调用会增加测试时间，不过不影响测试结果
        #使用谷歌浏览器
        driver=webdriver.Chrome()
        #访问地址
        driver.get("http://1.116.16.39:8081/index#")
        time.sleep(2)
        driver.find_element(By.NAME,"account").send_keys("admin")
        driver.find_element(By.NAME,"password").send_keys("123456")
        driver.find_element(By.XPATH,"//div[@class='login-container']/form/button").click()
        h=driver.get_cookies()
        # cookie保存到cookies.txt文件
        f1 = open("cookies.txt", "w")
        f1.write(json.dumps(h))
        f1.close
        print(h)
        print(type(h))

        # #关闭网页
        # driver.close()

    def login_cookies(self):
        #缓存免登录

        filexpath = get_local.get_cwd()
        f2 = open(filexpath + "\cookies.txt")
        cookies = json.loads(f2.read())
        # 使用cookies登录
        for cook in cookies:
            self.driver.add_cookie(cook)
        # 刷新页面
        self.driver.refresh()
        f2.close()
        time.sleep(3)


