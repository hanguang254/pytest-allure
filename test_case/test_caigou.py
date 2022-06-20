import os
from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import basepage
from test_object.Page import LoginPage
from common import img_class

class Test_01:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver   #全局用例的浏览器调用
        self.log=basepage.BasePage().get_log()
        self.log.info("正常启动")
    def teardwon_class(self):
        self.log.info("测试完成")
        self.driver.close()

    @allure.story("采购流程")
    def test_01(self,login):    #全局登录用例调用login
        sleep(2)
        with allure.step("点击采购管理"):
            self.log.info("点击采购合同")
            self.driver.find_element(By.XPATH, "//i[@class='fa fa-shopping-cart']").click()
            self.driver.find_element(By.XPATH, "//a[@text='采购合同']").click()
            sleep(5)
        with allure.step("新增合同"):
            self.log.info("新增合同")
            self.driver.find_element(By.XPATH, "//button[@opr-permission='803']").click()
            sleep(5)
            self.driver.find_element(By.XPATH, "//input[contains(@class,'form-control readonly')]").send_keys(
                "江阴辰田金属科技有限公司")
            sleep(2)
            self.driver.find_element(By.XPATH, "(//input[contains(@class,'form-control readonly')])[2]").send_keys("金冠")
            sleep(2)
            self.log.info("选择物资")
            self.driver.find_element(By.XPATH, "//div[@id='purchaseContractContainer_addPurchaseContractModal']"
                                               "/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]"
                                               "/div[1]/div[1]/button[1]/i[1]").click()
            sleep(5)
            self.driver.find_element(By.XPATH, "//td[text()='低合金板']").click()
            self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-primary')]//i[1]").click()
            self.log.info("填写物资明细")
            sleep(2)
            self.driver.find_element(By.XPATH, "(//td[@class='required editable-column'])[2]").send_keys(1, Keys.ENTER)
            sleep(2)
            self.driver.find_element(By.XPATH, "(//td[@class='required editable-column'])[3]").send_keys(2, Keys.ENTER)
            sleep(2)
            self.driver.find_element(By.XPATH, "//td[text()='0.00']").send_keys(2, Keys.ENTER)
            sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()[normalize-space()='保存']]").click()
            self.log.info("保存成功，刷新单据明细")
            sleep(3)
            img_class.test_img(self.driver).Play_img() #保存截图
            self.log.info("截图保存成功")

if __name__ == '__main__':
        # pytest.main(["test_caigou.py","-sv"])
        result_dir = "../log_out/json"  # json存储位置
        report_dir = "../log_out/report_test"  # 报告存储位置
        pytest.main(["-sv", "--alluredir=%s" % result_dir, "--clean-alluredir", "test_caigou.py"])     #测试用例文件
        os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))   #allure报告的输出