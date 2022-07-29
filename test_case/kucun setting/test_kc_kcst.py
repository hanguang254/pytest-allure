from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_object.Page import LoginPage


class Test_kcst:

    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()

        
    def teardown_class(self):
        self.driver.close()


    def test_kcst(self,login):
        #采购管理—库存实体
        sleep(3)
        self.driver.find_element(By.XPATH,"//a[@m='ckgl']").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[@href='#'][contains(text(),'库存实提')]").click()
        sleep(2)

        self.driver.find_element(By.XPATH,"//button[@id='addOutWhs']").click()
        sleep(1)
        #销售合同
        self.driver.find_element(By.XPATH,"//input[@name='salesContractNo']").send_keys(46452432)
        sleep(0.5)
        # 客户
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal_addOutWhsForm"]'
                                          '/label[8]/input').send_keys("舞钢钢铁（北京）有限公司")
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//strong[contains(text(),'舞钢钢铁（北京）有限公司')]").click()
        sleep(0.5)
        #仓库
        self.driver.find_element(By.XPATH,"//input[@name='whsId']").send_keys("长沙钢贸仓库")
        sleep(0.5)
        #经办人
        self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
        sleep(0.5)
        #协办人
        self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("测试1")
        sleep(0.5)
        #终端客户
        self.driver.find_element(By.XPATH, "//input[@name='main2']").send_keys("舞钢钢铁（北京）有限公司")
        sleep(0.5)
        # 业务机构
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal_addOutWhsForm"]'
                                          '/label[20]/input').send_keys("金冠")
        sleep(0.5)
        # 备注
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal_addOutWhsForm"]'
                                          '/label[23]/input').send_keys("自动化测试单据")
        sleep(0.5)

        #库存提单
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refSalesLadingExtBtnInOutWhs']").click()
        sleep(1)

        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_outWhs-importSalesLadingExt-div"]'
                                          '/div/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[9]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary saveSalesLadingBtn']").click()
        sleep(1)

        # 匹配码单
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div[1]/'
                                          'div[1]/div[2]/div[2]/table/tbody/tr/td[2]').click()
        sleep(0.5)
        # 匹配码单
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm outWhsReceiptTitleAutoMatchInExt']").click()
        sleep(0.5)

        # 费用明细
        self.driver.find_element(By.XPATH,"//a[@href='.SalesChargesTabInOutWhs']").click()
        sleep(0.5)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addOutWhsSalesCharges']").click()
        sleep(0.5)

        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div'
                                          '[1]/div[2]/div[2]/table/tbody/tr/td[4]').send_keys("应收")
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]'
                                          '/div[2]/div[2]/ul/li[1]/a').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]'
                                          '/div[2]/div[2]/table/tbody/tr/td[5]').send_keys("运输费")
        sleep(0.5)
        #费用单价
        self.driver.find_element(By.XPATH,'//*[@id="outWhsContainer_addOutWhsModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]'
                                          '/div[2]/div[2]/table/tbody/tr/td[11]').send_keys("34",Keys.ENTER)
        sleep(0.5)

        # 保存
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnOutWhs']").click()
        sleep(0.5)


        sleep(5)





if __name__ == '__main__':
    pytest.main(['-qsv','test_kc_kcst.py'])