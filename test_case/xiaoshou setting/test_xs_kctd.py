from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_object.Page import LoginPage



class Test_kctd:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.close()

    def test_kctd(self,login):
        # 打开销售管理-库存提单
        sleep(3)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'销售管理')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[@href='#'][contains(text(),'库存提单')]").click()
        sleep(2)

        #添加库存提单
        self.driver.find_element(By.XPATH,"//button[@id='addSalesLading2']").click()
        sleep(1)
        # 原始单据
        self.driver.find_element(By.XPATH,"//input[@name='originalNo']").send_keys(6773845)
        sleep(0.5)
        #客户
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal_addSalesLadingForm"]'
                                          '/label[7]/input').send_keys("江阴金冠钢铁贸易有限公司")
        sleep(0.5)
        # 仓库
        self.driver.find_element(By.XPATH,"//input[@name='whsId']").send_keys("长沙钢贸仓库")
        sleep(0.5)
        # 经办人
        self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
        sleep(0.5)
        #协办人
        self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("测试1")
        sleep(0.5)
        #业务机构
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal_addSalesLadingForm"]'
                                          '/label[18]/input').send_keys("金冠")
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal_addSalesLadingForm"]'
                                          '/label[18]/ul/li[1]/a/strong').click()
        #打印次数
        self.driver.find_element(By.XPATH,"//input[@name='main5']").send_keys(1)
        #备注
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal_addSalesLadingForm"]'
                                          '/label[24]/input').send_keys("自动化测试单据")
        #引用物资明细
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm refGoodsListBtnInSalesLading']").click()
        sleep(1.5)
        # 选择物资
        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2200*L')]").click()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'10*2500*L')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary validateSelectGoodsPurchaseContract']").click()
        sleep(1)
        #手动添加
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addSalesLadingExt']").click()

        # 品名
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[6]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'低合金板')]").click()
        sleep(0.5)
        # 规格
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[7]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='10*2200*L']").click()
        sleep(0.5)
        # 材质
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[8]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Q355B']").click()
        sleep(0.5)
        # 产地
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[9]').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[@role='option'][contains(text(),'南钢')]").click()


        # 填写明细
        # 仓库
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr[1]/td[5]').send_keys("长沙钢贸仓库")
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                          'div[2]/ul/li[1]/a').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[5]').send_keys("长沙钢贸仓库")
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                          'div[2]/ul/li[1]/a').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[5]').send_keys("长沙钢贸仓库")
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/ul/li[1]/a').click()
        sleep(0.5)
        #数量
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[1]/td[13]').send_keys(1, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[13]').send_keys(2, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[13]').send_keys(3, Keys.ENTER)
        sleep(0.5)
        # 吨位
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[1]/td[14]').send_keys(3, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[14]').send_keys(3, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[14]').send_keys(3, Keys.ENTER)
        sleep(0.5)
        #销售单价
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr[1]/td[15]').send_keys(1000,Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[15]').send_keys(1000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[15]').send_keys(1000, Keys.ENTER)
        sleep(0.5)
        # 费用单价
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[1]/td[18]').send_keys(1000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[18]').send_keys(1000, Keys.ENTER)
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[3]/td[18]').send_keys(1000, Keys.ENTER)
        sleep(0.5)

        #保存
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnSalesLading']").click()
        sleep(2)

        #修改单据
        self.driver.find_element(By.XPATH,"//td[contains(text(),'自动化测试单据')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@id='updateSalesLading2']").click()
        sleep(1)

        self.driver.find_element(By.XPATH,"//a[@role='tab'][contains(text(),'费用明细')]").click()
        a=self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addSalesLadingSalesCharges']")
        # 双击
        ActionChains(self.driver).double_click(a).perform()

        # 费用系数
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr[1]/td[7]').send_keys("0.95")
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='0.95']").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[7]').send_keys("0.95")
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='0.95']").click()
        sleep(0.5)
        # 单价
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr[1]/td[11]').send_keys(35,Keys.ENTER)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[11]').send_keys(35,Keys.ENTER)
        sleep(0.5)
        # 费用单位
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr[1]/td[14]').send_keys("江阴辰田金属科技有限公司")
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'江阴辰田金属科技有限公司')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                           '/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/'
                                           'div[2]/table/tbody/tr[2]/td[14]').send_keys("江阴辰田金属科技有限公司")
        sleep(0.5)
        self.driver.find_element(By.XPATH, "//strong[contains(text(),'江阴辰田金属科技有限公司')]").click()
        sleep(0.5)

        #运输明细
        self.driver.find_element(By.XPATH,"//a[contains(text(),'运输明细')]").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm addSalesLadingTransportDetail']").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,'//*[@id="salesLadingContainer2_addSalesLadingModal"]'
                                          '/div/div/div[3]/div[3]/div/div[3]/div/div[1]/div[2]/'
                                          'div[2]/table/tbody/tr/td[6]').send_keys(45434)


        sleep(1)
        # 保存
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnSalesLading']").click()
        sleep(3)

        #作废单据
        self.driver.find_element(By.XPATH, "//td[contains(text(),'自动化测试单据')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@id='deleteSalesLading2']").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//button[@name='btn_ok']").click()
        sleep(2)

if __name__ == '__main__':
    pytest.main(['-qv','test_xs_kctd.py'])