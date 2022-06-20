from selenium.webdriver.common.by import By

#登录全局用例参数

url="http://1.116.16.39:8081/"        #测试地址

uesr={
    "username":("ceshi"),             #后台系统账户
    "password":("123456")
}

login={
    "zhanghao":(By.XPATH, "//input[@class='form-control']"),   #账户xpath
    "password":(By.XPATH, "//input[@name='password']"),       #密码xpath
    "denglu":(By.XPATH,"//button")                            #登录xpath
}
