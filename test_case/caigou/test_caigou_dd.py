from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_object.Page import LoginPage
from common import basepage



class Test_caigou_dd:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.log=basepage.BasePage().get_log()
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.close()

    def test_dd(self,login):
        sleep(4)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'采购管理')]").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"//a[@m='cgdd']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="addPurchaseSend2"]/i').click()
        self.log.info("正在填写物资单据")
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal_addPurchaseSendForm"]'
                                          '/label[8]/input').send_keys("江阴辰田金属科技有限公司")
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'江阴辰田金属科技有限公司')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='purchaseContractNo']").send_keys(4564564564)
        self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
        sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("测试1")
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//input[@name='instId']").send_keys("金冠")
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal_addPurchaseSendForm"]'
                                          '/label[19]/input').send_keys("自动化测试单据")
        self.log.info("正在选择物资")
        sleep(1)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refGoodsListBtnInPurchaseSend']").click()
        sleep(3)

        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2200*L')]").click()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2500*L')]").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-primary')]//i[1]").click()
        self.log.info("正在填写明细")
        sleep(1)
        # 数量填写
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[10]').send_keys(1, Keys.ENTER)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[10]').send_keys(2, Keys.ENTER)
        # 吨位填写
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[11]').send_keys(3, Keys.ENTER)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[11]').send_keys(6, Keys.ENTER)
        # 单价填写
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[12]').send_keys(1000,Keys.ENTER)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[12]').send_keys(2000,Keys.ENTER)

        self.log.info("正在删除物资，新增物资")
        # 删除物资
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[2]/td[3]/a').click()

        sleep(1)
        # 手动添加物资
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-sm addPurchaseSendExt']").click()
        # 品名
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[4]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'低合金板')]").click()
        sleep(1)
        # 规格
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[5]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='10*2500*L']").click()
        sleep(1)
        # 材质
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[6]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Q355B']").click()
        sleep(1)
        # 产地
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[7]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[@role='option'][contains(text(),'南钢')]").click()
        # 数量
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[10]').send_keys(2, Keys.ENTER)
        # 吨位
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[11]').send_keys(10, Keys.ENTER)
        # 单价
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[12]').send_keys(2000)
        #保存单据
        self.log.info("保存单据")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseSend']").click()
        sleep(2)

        #修改单据
        self.log.info("选择单据修改")
        self.driver.find_element(By.XPATH,"//td[contains(text(),'自动化测试单据')]").click()
        #修改按钮
        self.driver.find_element(By.XPATH,"//button[@id='updatePurchaseSend2']").click()
        sleep(1)
        #费用明细
        self.driver.find_element(By.XPATH,"//a[@role='tab'][contains(text(),'费用明细')]").click()
        sleep(0.5)

        a=self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addPurchaseSendSalesCharges']")
        #双击操作
        ActionChains(self.driver).double_click(a).perform()
        #运输类型
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[5]').send_keys("运输费")
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[5]').send_keys("运输费")
        sleep(0.5)
        #费用计算类型
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[6]').send_keys("按车次结算重量")
        sleep(0.5)

        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[6]').send_keys("按车次结算重量")
        sleep(0.5)
        # 费用单位类型
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[7]').send_keys("元/吨")
        sleep(0.5)

        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[7]').send_keys("元/吨")
        sleep(0.5)
        # 结算方式
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[8]').send_keys("现汇")
        sleep(0.5)

        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[8]').send_keys("现汇")
        sleep(0.5)
        #含税单价
        self.driver.find_element(By.XPATH,'//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[11]').send_keys(345,Keys.ENTER)
        sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="purchaseSendContainer2_addPurchaseSendModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[11]').send_keys(35)
        sleep(1)

        #保存修改
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseSend']").click()
        sleep(5)

if __name__ == '__main__':
    pytest.main(['-qsv','test_caigou_dd.py'])