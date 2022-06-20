from selenium.webdriver.common.by import By
from test_object.Element import login_local

class Login():

    def __init__(self,driver):
        self.driver=driver

    def login(self):

        self.driver.find_element(*login_local.login["zhanghao"]).send_keys("ceshi")
        self.driver.find_element(*login_local.login["password"]).send_keys("123456")
        self.driver.find_element(By.XPATH, "//button").click()