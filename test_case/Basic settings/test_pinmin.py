import os
from time import sleep
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_object.Page import pinmin_page
from test_object.Page import LoginPage
from common import basepage
from common import img_class

@allure.feature("品名流程")
class Test_pinmin:
    def setup_class(self):
        self.log=basepage.BasePage().get_log()
        self.driver=LoginPage.LoginPage().driver

    def tesrdwon_class(self):   #后置条件/
        self.log.info("流程测试完成")

    @allure.story("品名新增作废")
    def test_pinmin(self,login):
        with allure.step("选择品名设置"):
            self.log.info("引用全局用例登录")
            self.log.info("点击品名新增按钮")
            pinmin_page.pinmin_class(self.driver).shezhi()
        with allure.step("新增品名"):
            pinmin_page.pinmin_class(self.driver).canshu()
            self.log.info("保存采购，刷新单据")
        with allure.step("作废单据"):
            self.log.info("选择新增品名作废")
            pinmin_page.pinmin_class(self.driver).zuofei()
            sleep(2)
            img_class.test_img(self.driver).Play_img()
            self.log.info("保存采购已截图，存放log_out/img_test")


if __name__ == '__main__':
    pytest.main(['-sv','test_pinmin.py'])

    # result_dir = "../log_out/json"  # json存储位置
    # report_dir = "../log_out/report_test"  # 报告存储位置
    # pytest.main(["-sv", "--alluredir=%s" % result_dir, "--clean-alluredir", "test_pinmin.py"])  # 测试用例文件
    # os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))  # allure报告的输出