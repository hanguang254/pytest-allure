from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_object.Page import LoginPage
from common import basepage



class Test_rk:
    def setup_class(self):  #前置条件
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()    #全屏
        self.log=basepage.BasePage().get_log()

    def teardown_class(self):  #后置条件
        self.driver.close()

    def test_rk(self,login):
        try:
            self.log.info("正在打开采购入库")
            sleep(3)
            self.driver.find_element(By.XPATH,"//span[contains(text(),'采购管理')]").click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//a[@m='cgrk']").click()
            sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="addPurchaseInWhs"]').click()
            sleep(2)

            #添加采购入库单据
            self.log.info("正在填写主单据")
            self.driver.find_element(By.XPATH,'//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal_addPurchaseInWhsForm"]'
                                              '/label[5]/input').send_keys("456546456") #采购合同号
            sleep(0.5)
            self.driver.find_element(By.XPATH,"//input[@name='whsId']").send_keys("长沙钢贸仓库") #仓库
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal_addPurchaseInWhsForm"]'
                                              '/label[11]/input').send_keys("江阴辰田金属科技有限公司") #供应商
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal_addPurchaseInWhsForm"]'
                                              '/label[12]/input').send_keys("自动化测试单据") #备注
            sleep(0.5)
            self.driver.find_element(By.XPATH,"//input[@name='instId']").send_keys("金冠") #业务机构
            sleep(0.5)

            #引用物资明细
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refGoodsListBtnInPurchaseInWhs']").click()
            sleep(2)
            #选择物资
            self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2200*L')]").click()
            self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2500*L')]").click()
            #选择按钮
            self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-primary')]//i[1]").click()


            # 数量填写
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[13]').send_keys(1, Keys.ENTER)
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[13]').send_keys(2, Keys.ENTER)
            # 吨位填写
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[14]').send_keys(3, Keys.ENTER)
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[14]').send_keys(6, Keys.ENTER)
            #结算数量
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[1]/td[15]').send_keys(1,Keys.ENTER)

            #结算重量
            sleep(0.5)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[1]/td[16]').send_keys(3,Keys.ENTER)

            # 单价填写
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[18]').send_keys(1000, Keys.ENTER)
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[18]').send_keys(2000, Keys.ENTER)

            self.log.info("正在删除物资，新增物资")
            # 删除物资
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[3]/a').click()

            #手动添加
            sleep(0.5)
            #添加按钮
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addPurchaseInWhsExt']").click()
            sleep(0.5)
            # 品名
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[6]').click()
            sleep(0.5)
            self.driver.find_element(By.XPATH, "//a[contains(text(),'低合金板')]").click()
            sleep(0.5)
            # 规格
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[7]').click()
            sleep(0.5)
            self.driver.find_element(By.XPATH, "//a[normalize-space()='10*2500*L']").click()
            sleep(0.5)
            # 材质
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[8]').click()
            sleep(0.5)
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Q355B']").click()
            sleep(0.5)
            # 产地
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[9]').click()
            sleep(0.5)
            self.driver.find_element(By.XPATH, "//a[@role='option'][contains(text(),'南钢')]").click()
            # 数量
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[13]').send_keys(2, Keys.ENTER)
            # 吨位
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[14]').send_keys(10, Keys.ENTER)
            # 结算数量
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[15]').send_keys(2, Keys.ENTER)

            # 结算重量
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[16]').send_keys(10, Keys.ENTER)
            # 单价
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[18]').send_keys(2000,Keys.ENTER)
            sleep(0.5)
            #保存按钮
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseInWhs']").click()
            self.log.info("采购入库单据保存成功")

            self.log.info("正在修改单据")
            #修改单据
            sleep(2)
            self.driver.find_element(By.XPATH,"//td[contains(text(),'自动化测试单据')]").click() #点击单据
            sleep(1)
            #修改按钮
            self.driver.find_element(By.XPATH,"//button[@id='updatePurchaseInWhs']").click()
            sleep(1)
            #费用明细
            self.driver.find_element(By.XPATH,"//a[@role='tab'][contains(text(),'费用明细')]").click()
            sleep(0.5)
            b=self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addPurchaseInWhsSalesCharges']")
            ActionChains(self.driver).double_click(b).perform() #双击

            # 运输类型
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[5]').send_keys("运输费")
            sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[5]').send_keys("运输费")
            sleep(0.5)
            # 费用计算类型
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[6]').send_keys("按车次结算重量")
            sleep(0.5)

            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[6]').send_keys("按车次结算重量")
            sleep(0.5)
            # 费用单位类型
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[7]').send_keys("元/吨")
            sleep(0.5)

            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[7]').send_keys("元/吨")
            sleep(0.5)
            # 结算方式
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[8]').send_keys("现汇")
            sleep(0.5)

            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[8]').send_keys("现汇")
            sleep(0.5)
            # 含税单价
            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[1]/td[11]').send_keys(345, Keys.ENTER)
            sleep(1)

            self.driver.find_element(By.XPATH, '//*[@id="purchaseInWhsContainer_addPurchaseInWhsModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[11]').send_keys(35)
            sleep(1)
            #保存修改
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseInWhs']").click()
            self.log.info("单据修改成功")


            sleep(5)
        except Exception as  e:
            self.log.error(e)


if __name__ == '__main__':
    pytest.main(['-qsv','test_caigou_rk.py'])