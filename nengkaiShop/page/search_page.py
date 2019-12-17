from base.base_page import BasePage


class SearchComm(BasePage):
    def search(self):
        '''搜索商品'''
        driver = self.base_driver
        driver.type('skeywords','手机')
        driver.open_new_window('x,/html/body/div[2]/div[1]/div[2]/form/input[2]')
        driver.sleep(3)
        driver.click('x,/html/body/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[2]/a/dl/dd/img')
        driver.maximize_window()
        driver.sleep(3)
        driver.click('x,/html/body/div[6]/div[1]/div[2]/div[1]/a[1]/em')


if '__main__' == __name__:

     #vv = SearchComm('Chrome')
    d = SearchComm('Chrome')
    # 输入网址
    d.navigate('https://shop.10086.cn/mall_100_100.html')
    d.search()