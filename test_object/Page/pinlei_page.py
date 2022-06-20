from time import sleep

from selenium.webdriver.common.by import By


class pinlei_page():
    def __init__(self,driver):
        self.driver=driver

    def pin_page(self):
        self.sleep=sleep(3)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'基础设置')]").click()
        self.sleep=sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'品类')]").click()
        self.sleep=sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id='addBrandClass']").click()
        self.sleep=sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='addFormBrandClass']/label[2]/select")
        self.sleep=sleep(1)

    def select_pin(self):
        self.driver.find_element(By.XPATH, "//*[@id='addFormBrandClass']/label[2]/select")

    def writer_class(self):
        self.sleep = sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div"
                                           "[2]/div[3]/div/div/div[3]/div[2]/div/form/label[3]/input").send_keys("测试板材")
    def baocun_pin(self):
        self.driver.find_element(By.XPATH, "//*[@id='addModalBrandClass']/div/div/div[4]/button[2]").click()
        self.sleep=sleep(3)
    def zuofei(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(),'测试板材')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='deleteBrandClass']").click()
        self.sleep=sleep(5)
        self.driver.find_element(By.XPATH, "//button[@name='btn_ok']").click()