import os
from time import sleep
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common import basepage
from test_object.Page import LoginPage
from test_object.Page import pinlei_page


@allure.feature("品类用例")
class Test_pinlei:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.log=basepage.BasePage().get_log()
        # self.sleep=sleep(1)

    def teardown_class(self):
        self.log.info("测试完成")

    @allure.story("品类新增作废")
    def test_pinlei(self,login):
        with allure.step("新增品类"):
            self.log.info("正在点击品名")
            pinlei_page.pinlei_page(self.driver).pin_page()
            self.log.info("正在输入品类值")
            #Select下拉框选择器
            Select(self.driver.find_element(By.XPATH, "//*[@id='addFormBrandClass']/label[2]/select")).select_by_value("板材")
            pinlei_page.pinlei_page(self.driver).writer_class()
        with allure.step("保存品类"):
            self.log.info("点击保存，刷新单据列表")
            pinlei_page.pinlei_page(self.driver).baocun_pin()

        with allure.step("作废新增品类"):
            pinlei_page.pinlei_page(self.driver).zuofei()
            self.log.info("作废成功，刷新单据")


if __name__ == '__main__':
    # pytest.main(["test_pinlei.py","-sv"])

    result_dir = "../../log_out/json"  # json存储位置
    report_dir = "../log_out/report_pinlei_test"  # 报告存储位置
    pytest.main(["-sv", "--alluredir=%s" % result_dir, "--clean-alluredir", "test_pinlei.py"])  # 测试用例文件
    os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))  # allure报告的输出

    # pytest.main(['-s', '-vv', 'test_pinlei.py', '--alluredir', '../log_out/report_test1'])