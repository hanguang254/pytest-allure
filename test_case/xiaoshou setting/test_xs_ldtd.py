from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_object.Page import LoginPage



class Test_ldtd:
    def setup_class(self):
        self.driver=LoginPage.LoginPage().driver
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.close()

    def test_ldtd(self,login):
        #临调提单
        sleep(3)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'销售管理')]").click()
        sleep(0.5)
        self.driver.find_element(By.XPATH,"//a[@href='#'][contains(text(),'临调提单')]").click()
        sleep(3)

        list=[6,7,8,9,12] #业务单据类型    value值

        for i in list:
            # print(type(i),i) #查看数据类型与输出结果

            self.driver.find_element(By.XPATH,"//button[@id='addTemporarySalesLading2']").click()
            sleep(1)
            # 业务类型
            Select(self.driver.find_element(By.XPATH,"//select[@class='form-control "
                                                     "readonly dict-select']")).select_by_value("{}".format(i))
            sleep(0.5)
            if i==8 or i==9:
                # 客户
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2_'
                                                   'addTemporarySalesLadingModal'
                                                   '_addTemporarySalesLadingForm"]'
                                                   '/label[8]/input').send_keys("江苏融汇通供应链管理有限公司")
                sleep(0.5)
                self.driver.find_element(By.XPATH, "//strong[contains(text(),'江苏融汇通供应链管理有限公司')]").click()
                sleep(0.5)
                # 供应商
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2'
                                                   '_addTemporarySalesLadingModal_addTemporarySalesLadingForm"]'
                                                   '/label[9]/input').send_keys("江阴辰田金属科技有限公司")
                sleep(1)
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2'
                                                   '_addTemporarySalesLadingModal_addTempora'
                                                   'rySalesLadingForm"]/label[9]/ul/li[1]/a').click()
                sleep(0.5)
                #终端客户
                self.driver.find_element(By.XPATH,"//input[@name='main2']").send_keys("舞钢钢铁（北京）有限公司")
                sleep(1)

                # 经办人
                self.driver.find_element(By.XPATH, "//input[@name='main3']").send_keys("管理员")
                sleep(1)
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2'
                                                  '_addTemporarySalesLadingModal_addTemporar'
                                                  'ySalesLadingForm"]/label[12]/ul/li[1]/a').click()
                sleep(0.5)
                # 协办人
                self.driver.find_element(By.XPATH, "//input[@name='main4']").send_keys("测试1")
                sleep(0.5)
                # 业务结构
                self.driver.find_element(By.XPATH, "//form[@id='temporarySalesLadingContainer2"
                                                   "_addTemporarySalesLadingModal_addTemporarySalesLadingForm']"
                                                   "//input[@name='instId']").send_keys("金冠")
                sleep(0.5)
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2'
                                                   '_addTemporarySalesLadingModal_addTemporarySalesLadingForm"]'
                                                   '/label[22]/input').send_keys("自动化测试单据")
                sleep(0.5)

                # 引用库存汇总
                self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-sm"
                                                   " refInventorySumBtnInTemporarySalesLading']").click()
                sleep(1)
                # 选择库存
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2_'
                                                   'temporarySalesLading-importInventorySum-div"]'
                                                   '/div/div/div/div[3]/div/div[1]/div/div[2]/'
                                                   'div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                sleep(0.5)
                self.driver.find_element(By.XPATH,
                                         "//button[@class='btn btn-primary validateSelectInventorySumList']").click()
                sleep(1)
                # 数量
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2_'
                                                   'addTemporarySalesLadingModal"]/div/div/div'
                                                   '[3]/div[3]/div/div[1]/div/div[1]/div[2]/div'
                                                   '[2]/table/tbody/tr/td[13]').send_keys(1, Keys.ENTER)
                sleep(1)
                # 吨位
                self.driver.find_element(By.XPATH, '//*[@id="temporarySalesLadingContainer2'
                                                   '_addTemporarySalesLadingModal"]'
                                                   '/div/div/div[3]/div[3]/div/div[1]/div/'
                                                   'div[1]/div[2]/div[2]/table/tbody/tr/td[14]').send_keys(1,
                                                                                                           Keys.ENTER)
                sleep(0.5)
                #终端单价
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2_'
                                                  'addTemporarySalesLadingModal"]/div/div/div'
                                                  '[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]'
                                                  '/table/tbody/tr/td[16]').send_keys(5555,Keys.ENTER)
                sleep(0.5)
                # 保存
                self.driver.find_element(By.XPATH,
                                         "//button[@class='btn btn-default btn-sm saveBtnTemporarySalesLading']").click()

                sleep(3)
            else:
                # 客户
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2_'
                                                  'addTemporarySalesLadingModal'
                                                  '_addTemporarySalesLadingForm"]'
                                                  '/label[8]/input').send_keys("江阴金冠钢铁贸易有限公司")
                sleep(0.5)
                self.driver.find_element(By.XPATH,"//strong[contains(text(),'江阴金冠钢铁贸易有限公司')]").click()
                sleep(0.5)
                #供应商
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2'
                                                  '_addTemporarySalesLadingModal_addTemporarySalesLadingForm"]'
                                                  '/label[9]/input').send_keys("江阴辰田金属科技有限公司")
                sleep(1)
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2'
                                                  '_addTemporarySalesLadingModal_addTempora'
                                                  'rySalesLadingForm"]/label[9]/ul/li[1]/a').click()
                sleep(0.5)
                #经办人
                self.driver.find_element(By.XPATH,"//input[@name='main3']").send_keys("管理员")
                sleep(0.5)
                #协办人
                self.driver.find_element(By.XPATH,"//input[@name='main4']").send_keys("测试1")
                sleep(0.5)
                #业务结构
                self.driver.find_element(By.XPATH,"//form[@id='temporarySalesLadingContainer2"
                                                  "_addTemporarySalesLadingModal_addTemporarySalesLadingForm']"
                                                  "//input[@name='instId']").send_keys("金冠")
                sleep(0.5)
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2'
                                                  '_addTemporarySalesLadingModal_addTemporarySalesLadingForm"]'
                                                  '/label[22]/input').send_keys("自动化测试单据")
                sleep(0.5)

                #引用库存汇总
                self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm"
                                                  " refInventorySumBtnInTemporarySalesLading']").click()
                sleep(1)
                #选择库存
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2_'
                                                  'temporarySalesLading-importInventorySum-div"]'
                                                  '/div/div/div/div[3]/div/div[1]/div/div[2]/'
                                                  'div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                sleep(0.5)
                self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary validateSelectInventorySumList']").click()
                sleep(1)
                #数量
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2_'
                                                  'addTemporarySalesLadingModal"]/div/div/div'
                                                  '[3]/div[3]/div/div[1]/div/div[1]/div[2]/div'
                                                  '[2]/table/tbody/tr/td[13]').send_keys(1,Keys.ENTER)
                sleep(1)
                # 吨位
                self.driver.find_element(By.XPATH,'//*[@id="temporarySalesLadingContainer2'
                                                  '_addTemporarySalesLadingModal"]'
                                                  '/div/div/div[3]/div[3]/div/div[1]/div/'
                                                  'div[1]/div[2]/div[2]/table/tbody/tr/td[14]').send_keys(1,Keys.ENTER)
                sleep(0.5)
                # 保存
                self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm saveBtnTemporarySalesLading']").click()

                sleep(3)


if __name__ == '__main__':
    pytest.main(['-qsv','test_xs_ldtd.py'])