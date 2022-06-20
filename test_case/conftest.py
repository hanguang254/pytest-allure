import pytest
from test_object.Page import LoginPage
from test_object.Element import login_local

#全局用例

@pytest.fixture(scope='session',autouse=True)
def login():                            #全局用例的登录方法 ，直接调用无需导入文件
    login = LoginPage.LoginPage()
    login.url                           #打开网址
    login.username.send_keys(*login_local.uesr["username"])   #输入账户
    login.password.send_keys(*login_local.uesr["password"])  #输入密码
    login.submit.click()                #点击登录

    yield   #后置条件
    login.driver.close()  #关闭窗口

