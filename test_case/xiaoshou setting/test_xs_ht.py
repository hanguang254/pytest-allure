from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_object.Page import LoginPage



class Test_xs_ht:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.close()

    def test_xs_ht(self,login):
        #打开销售管理-销售合同
        sleep(3)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'销售管理')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[@m='xsht']").click()
        sleep(2)
        #添加合同
        self.driver.find_element(By.XPATH,"//button[@id='addSalesContract']").click()
        sleep(1)
        #客户
        self.driver.find_element(By.XPATH,'//*[@id="salesContractContainer_addSalesContractModal_addSalesContractForm"]'
                                          '/label[7]/input').send_keys("江阴金冠钢铁贸易有限公司")
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'江阴金冠钢铁贸易有限公司')]").click()
        #原始单据
        self.driver.find_element(By.XPATH,"//input[@name='originalNo']").send_keys(34534534534)
        sleep(0.5)
        #经办人
        self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
        sleep(0.5)
        #协办人
        self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("测试1")
        sleep(0.5)
        #机构
        self.driver.find_element(By.XPATH,"//input[@name='instId']").send_keys("金冠")
        sleep(0.5)
        #备注
        self.driver.find_element(By.XPATH,'//*[@id="salesContractContainer_addSalesContractModal_addSalesContractForm"]'
                                          '/label[13]/input').send_keys("自动化测试单据")
        #约定回款日
        self.driver.find_element(By.XPATH,"//input[@name='main6']").send_keys(5)
        #结算方式
        self.driver.find_element(By.XPATH,"//input[@name='main7']").send_keys("现汇")
        #交货方式
        self.driver.find_element(By.XPATH,"//input[@name='main8']").send_keys("汽运")
        #合同履行地
        self.driver.find_element(By.XPATH,"//input[@name='main9']").send_keys("长沙")

        #引用物资
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refGoodsListBtnInSalesContract']").click()
        sleep(2)
        # 选择物资
        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2200*L')]").click()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2500*L')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary validateSelectGoodsPurchaseContract']").click()
        #手动添加
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addSalesContractExt']").click()
        sleep(0.5)
        # 品名
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[4]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'低合金板')]").click()
        sleep(0.5)
        # 规格
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[5]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='10*2500*L']").click()
        sleep(0.5)
        # 材质
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[6]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Q355B']").click()
        sleep(0.5)
        # 产地
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[7]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[@role='option'][contains(text(),'南钢')]").click()


        #物资明细
        #数量
        self.driver.find_element(By.XPATH,'//*[@id="salesContractContainer_addSalesContractModal"]'
                                          '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[1]/td[11]').send_keys(1,Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesContractContainer_addSalesContractModal"]'
                                          '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[2]/td[11]').send_keys(2,Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[11]').send_keys(3,Keys.ENTER)
        sleep(0.5)
        #吨位
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[12]').send_keys(4, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[12]').send_keys(4, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[12]').send_keys(4, Keys.ENTER)
        sleep(0.5)
        #含税单价
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[13]').send_keys(1000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[13]').send_keys(2000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[13]').send_keys(3000, Keys.ENTER)
        sleep(0.5)
        # 备注
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[1]/td[15]').send_keys("自动化",Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[2]/td[15]').send_keys("自动化", Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[15]').send_keys("自动化", Keys.ENTER)
        sleep(0.5)
        # 删除物资
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="salesContractContainer_addSalesContractModal"]'
                                          '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                          '/table/tbody/tr[3]/td[3]/a').click()
        sleep(0.5)
        #保存
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnSalesContract']").click()
        sleep(2)

        #修改单据
        self.driver.find_element(By.XPATH,'//*[@id="salesContractTable"]/tbody/tr[1]/td[15]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@id='updateSalesContract']").click()
        sleep(1)

        # 手动添加
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-sm addSalesContractExt']").click()
        sleep(0.5)
        # 品名
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[4]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'低合金板')]").click()
        sleep(0.5)
        # 规格
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[5]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='10*2500*L']").click()
        sleep(0.5)
        # 材质
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[6]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Q355B']").click()
        sleep(0.5)
        # 产地
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[7]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[@role='option'][contains(text(),'南钢')]").click()

        #数量吨位价格
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[11]').send_keys(3, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[12]').send_keys(4, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[13]').send_keys(3000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesContractContainer_addSalesContractModal"]'
                                           '/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]'
                                           '/table/tbody/tr[3]/td[15]').send_keys("自动化", Keys.ENTER)
        sleep(0.5)
        # 保存
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-sm saveBtnSalesContract']").click()
        sleep(3)




if __name__ == '__main__':
    pytest.main(['-qv','test_xs_ht.py'])
