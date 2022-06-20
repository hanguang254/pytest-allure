import time

from log_out import get_local

class test_img():
    def __init__(self,driver):
        self.driver=driver

    def Play_img(self):
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        d = get_local.get_cwd() + r"\img_test" +"\\"+rq+ ".png"
        self.driver.get_screenshot_as_file(d)
        return rq+"png"


# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# d = get_local.get_cwd()+r"\test_img"+"\\"+rq+ ".png"
# print(d)