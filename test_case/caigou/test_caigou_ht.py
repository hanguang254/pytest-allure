from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_object.Page import LoginPage
from common import basepage
from common import img_class

class Test_caigou_ht:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.log=basepage.BasePage().get_log()

    def test_ht(self,login):
        try:
            sleep(4)
            self.driver.find_element(By.XPATH, "//i[@class='fa fa-shopping-cart']").click()
            self.driver.find_element(By.XPATH, "//a[@text='采购合同']").click()
            sleep(3)
            self.log.info("新增合同,填写主单据")
            self.driver.find_element(By.XPATH, "//button[@opr-permission='803']").click()
            sleep(3)
            self.driver.find_element(By.XPATH, "//input[contains(@class,'form-control readonly')]").send_keys(
                "江阴辰田金属科技有限公司")
            sleep(2)
            self.driver.find_element(By.XPATH, "(//input[contains(@class,'form-control readonly')])[2]").send_keys("金冠")
            sleep(2)
            self.driver.find_element(By.XPATH,"//form[@class='grid form-modal form-container form-group-xs']"
                                              "/label[7]/input").send_keys(111111)
            self.driver.find_element(By.XPATH,"//form[@class='grid form-modal form-container form-group-xs']"
                                              "/label[12]/input").send_keys(22)
            self.driver.find_element(By.XPATH, "//form[@class='grid form-modal form-container form-group-xs']"
                                               "/label[13]/input").send_keys(22)
            self.driver.find_element(By.XPATH, "//form[@class='grid form-modal form-container form-group-xs']"
                                               "/label[14]/input").send_keys("自动化测试数据单")
            self.log.info("选择物资")
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refGoodsListBtnInPurchaseContract']").click()
            sleep(3)
            self.driver.find_element(By.XPATH,"//td[contains(text(),'10*2200*L')]").click()
            self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2500*L')]").click()
            sleep(1)
            self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-primary')]//i[1]").click()
            self.log.info("填写明细")
            sleep(1)
            #数量填写
            self.driver.find_element(By.XPATH,"//*[@id='purchaseContractContainer_addPurchaseContractModal']"
                                              "/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table"
                                              "/tbody/tr[1]/td[12]").send_keys(1,Keys.ENTER)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table'
                                              '/tbody/tr[2]/td[12]').send_keys(2,Keys.ENTER)
            # 吨位填写
            sleep(1)
            self.driver.find_element(By.XPATH,"//*[@id='purchaseContractContainer_addPurchaseContractModal']"
                                              "/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table"
                                              "/tbody/tr[1]/td[13]").send_keys(3,Keys.ENTER)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table/'
                                              'tbody/tr[2]/td[13]').send_keys(6,Keys.ENTER)
            #单价填写
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[@id='purchaseContractContainer_addPurchaseContractModal']"
                                               "/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table"
                                               "/tbody/tr[1]/td[14]").send_keys(1000)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table'
                                              '/tbody/tr[2]/td[14]').send_keys(2000)

            self.log.info("正在删除物资，新增物资")
            # 删除物资
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table'
                                              '/tbody/tr[2]/td[2]').click()
            #删除按钮
            # self.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-sm delPurchaseContractExt"]').click()
            sleep(1)
            # 删除标签
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table'
                                              '/tbody/tr[2]/td[3]/a').click()
            #手动添加物资
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addPurchaseContractExt']").click()
            #品名
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/table'
                                              '/tbody/tr[2]/td[4]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//a[contains(text(),'低合金板')]").click()
            sleep(1)
            #规格
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/'
                                              'table/tbody/tr[2]/td[5]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//a[normalize-space()='10*2500*L']").click()
            sleep(1)
            #材质
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/'
                                              'table/tbody/tr[2]/td[6]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//a[normalize-space()='Q355B']").click()
            sleep(1)
            #产地
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[2]/td[7]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//a[@role='option'][contains(text(),'南钢')]").click()
            #数量
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/'
                                              'table/tbody/tr[2]/td[12]').send_keys(2,Keys.ENTER)
            #吨位
            sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[2]/td[13]').send_keys(10,Keys.ENTER)
            #单价
            sleep(2)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[2]/td[14]').send_keys(2000)

            self.log.info("保存单据")
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseContract']").click()
            sleep(5)
            self.log.info("修改单据")
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractTable"]/tbody/tr[1]/td[16]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//button[@id='updatePurchaseContract']").click()
            sleep(1)
            #托盘资金
            self.driver.find_element(By.XPATH,"//a[contains(text(),'托盘资金明细')]").click()
            sleep(1)
            #添加按钮
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addTrayFollowExt']").click()
            self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-sm addTrayFollowExt']").click()
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[1]/td[5]').send_keys(34534)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[2]/td[5]').send_keys(1231)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[1]/td[6]').send_keys("2022/06/21",Keys.ENTER)
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                               '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                               '/table/tbody/tr[2]/td[6]').send_keys("2022/06/21",Keys.ENTER)
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="purchaseContractContainer_addPurchaseContractModal"]'
                                              '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/div[2]'
                                              '/table/tbody/tr[2]/td[3]/a').click()
            #保存
            sleep(1)
            self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnPurchaseContract']").click()
            self.log.info("修改成功")
            # 作废单据
            sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="purchaseContractTable"]/tbody/tr[1]/td[16]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//button[@id='deletePurchaseContract']").click()
            sleep(1)
            self.driver.find_element(By.XPATH,"//button[@name='btn_ok']").click()
            self.log.info("作废成功")
            sleep(3)

        except Exception as E:
            self.log.error(E)
            img_class.test_img(self.driver).Play_img()
            self.log.info("错误时的截图已保存")


if __name__ == '__main__':
    pytest.main(['-qsv','test_caigou_ht.py'])  #-q不输出环境信息   —s输出login日志  -v输出更多详情信息