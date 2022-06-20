from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class pinmin_class():
    def __init__(self,driver):
        self.driver=driver
    def shezhi(self):
        self.sleep=sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'基础设置')]").click()
        self.sleep=sleep(1)
        self.driver.find_element(By.XPATH, "//body/div[1]/aside[1]/section[1]/ul[1]/li[13]/ul[1]/li[5]/a[1]").click()
        self.sleep=sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='addBrand']").click()

    def canshu(self):
        self.sleep=sleep(2)
        self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[2]/input").send_keys("测试品名")
        self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[5]/input").send_keys("板材", Keys.ENTER)

        # Select选择器
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[6]/select")).select_by_value("1")
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[7]/select")).select_by_value("1")
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[8]/select")).select_by_value("1")
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[9]/select")).select_by_value("1")
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[10]/select")).select_by_value("1")
        Select(self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[13]/select")).select_by_value("1")

        self.driver.find_element(By.XPATH, "//form[@id='addFormBrand']/label[16]/input").send_keys("234234")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary saveBrandBtn']").click()
        self.sleep = sleep(3)
    def zuofei(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(),'测试品名')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='deleteBrand']").click()
        self.sleep=sleep(2)
        self.driver.find_element(By.NAME, "btn_ok").click()