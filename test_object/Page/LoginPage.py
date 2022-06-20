from selenium import webdriver
from selenium.webdriver.common.by import By
from test_object.Element import login_local  #引用元素


class LoginPage():
    driver=webdriver.Chrome()
    url=driver.get(login_local.url)  #访问网址
    username=driver.find_element(*login_local.login["zhanghao"])    #账户
    password=driver.find_element(*login_local.login["password"])    #密码
    submit=driver.find_element(*login_local.login["denglu"])        #登录按钮

