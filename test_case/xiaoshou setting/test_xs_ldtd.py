from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_object.Page import LoginPage



class Test_ldtd:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.close()

    def test_ldtd(self,login):
        #临调提单
        sleep(3)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'销售管理')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[@href='#'][contains(text(),'临调提单')]").click()
        sleep(3)

        list=[6,7,8,9,12]

        # for i in range(0,len(list)):

        self.driver.find_element(By.XPATH,"//button[@id='addTemporarySalesLading2']").click()
        sleep(1)
        # 业务类型
        Select(self.driver.find_element(By.XPATH,"//select[@class='form-control readonly dict-select']")).select_by_value("6")
        sleep(0.5)
        # 客户
        self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2_addTemporarySalesLadingModal_addTemporarySalesLadingForm"]'
                                          '/label[8]/input').send_keys("江阴金冠钢铁贸易有限公司")
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'江阴金冠钢铁贸易有限公司')]").click()
        sleep(0.5)
        #供应商
        self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys("江阴辰田金属科技有限公司")
        sleep(0.5)
        #经办人
        self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
        sleep(0.5)
        #协办人
        self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("管理员")
        sleep(0.5)
        sleep(5)


if __name__ == '__main__':
    pytest.main(['-qv','test_xs_ldtd.py'])