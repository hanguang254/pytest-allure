import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import basepage
import pytest
import allure
from selenium import webdriver
from test_object.Page import login_page

@allure.feature("UI自动化")
class Test_UI:

    def setup_class(self):    #前置条件
        # self.driver=webdriver.Chrome()
        self.log=basepage.BasePage().get_log()
        # self.driver.get("http://1.116.16.39:8081/")

    def teardown_class(self):  #后置条件
        self.log.info("用例执行完成")
        self.driver.close()

    # @allure.story("登录成功")
    # @pytest.mark.run(order=1) #首先执行
    # def test_loging(self):
    #     try:
    #         self.log.info("执行登录")
    #         with allure.step("访问网址"):
    #             self.log.info("正在启动浏览器访问")
    #         with allure.step("输入账户密码"):
    #             sleep(4)
    #             # self.driver.find_element(By.XPATH,"//input[@class='form-control']").send_keys("ceshi")
    #             # self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("123456")
    #             # self.driver.find_element(By.XPATH,"//button").click()
    #             login_page.Login(self.driver).login()
    #         with allure.step("登录成功"):
    #             sleep(6)
    #             self.driver.find_element(By.XPATH, "//li[@class='tab-1 no-close active']/a").text
    #
    #             self.log.info("登录成功")
    #     except Exception as e:
    #         self.log.error(e)

    @allure.story("采购流程")
    @pytest.mark.run(order=2) #第二个执行
    def test_caigou(self,login):

        sleep(2)
        with allure.step("点击采购管理"):
            self.log.info("点击采购合同")
            self.driver.find_element(By.XPATH,"//i[@class='fa fa-shopping-cart']").click()
            self.driver.find_element(By.XPATH,"//a[@text='采购合同']").click()
            sleep(5)
        with allure.step("新增合同"):
            self.log.info("新增合同")
            self.driver.find_element(By.XPATH,"//button[@opr-permission='803']").click()
            sleep(5)
            self.driver.find_element(By.XPATH,"//input[contains(@class,'form-control readonly')]").send_keys("江阴辰田金属科技有限公司")
            self.driver.find_element(By.XPATH,"(//input[contains(@class,'form-control readonly')])[2]").send_keys("金冠")
            self.log.info("选择物资")
            self.driver.find_element(By.XPATH,"//div[@id='purchaseContractContainer_addPurchaseContractModal']"
                                              "/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]"
                                              "/div[1]/div[1]/button[1]/i[1]").click()
            sleep(5)
            self.driver.find_element(By.XPATH,"//td[text()='低合金板']").click()
            self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-primary')]//i[1]").click()
            self.log.info("填写物资明细")
            sleep(5)
            self.driver.find_element(By.XPATH,"(//td[@class='required editable-column'])[2]").send_keys(1,Keys.ENTER)
            sleep(5)
            self.driver.find_element(By.XPATH,"(//td[@class='required editable-column'])[3]").send_keys(2,Keys.ENTER)
            sleep(3)
            self.driver.find_element(By.XPATH,"//td[text()='0.00']").send_keys(2,Keys.ENTER)
            sleep(3)
            self.driver.find_element(By.XPATH,"//button[text()[normalize-space()='保存']]").click()
            self.log.info("保存成功，刷新单据明细")
            sleep(10)

if __name__ == '__main__':
    pytest.main(["-s","示例_test_JGUI.py"])


    # result_dir = "../log_out/json"  # json存储位置
    # report_dir = "../log_out/report_test"  # 报告存储位置
    # pytest.main(["-sv", "--alluredir=%s" % result_dir, "--clean-alluredir", "示例_test_JGUI.py"])
    # os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))