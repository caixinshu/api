from base.base_page import BasePage


class HomeShopPage(BasePage):
    def shop_floor_page(self):
        '''首页楼层购买手机'''
        driver = self.base_driver
        driver.sleep(3)
        # 点击购买的手机图片
        driver.drag_js('x,/html/body/div[4]/div[3]/div/ul/li[2]/div')
        driver.sleep(3)
        driver.open_new_window('x,/html/body/div[4]/div[3]/div/ul/li[2]/div/p[1]/a/img')
        # 【立即购买】
        driver.drag_js('x,//*[@id="buy_area"]/a[1]/em')
        driver.click('x,/html/body/div[6]/div[1]/div[2]/div[1]/a[1]/em')
        driver.sleep(10)



    def shop_list_page(self):
        '''首页表单购买手机'''
        driver = self.base_driver
        driver.sleep(3)
        # 点击购买的手机图片
        driver.click_by_text('买手机')
        print('选择列表手机')
        driver.sleep(3)
        driver.open_new_window('x,/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[1]/div[1]/a[1]')
        print('打开购买手机的新窗口')
        driver.drag_js('x,/html/body/div[5]/div[2]/div[4]/ul/li[1]/div/p[1]/a/img')
        print('聚焦手机')
        driver.open_new_window('x,/html/body/div[5]/div[2]/div[4]/ul/li[1]/div/p[1]/a/img')
        print('打开手机详情页')
        driver.sleep(3)
        # 【立即购买】
        driver.click('x,/html/body/div[6]/div[1]/div[2]/div[1]/a[1]/em')
        print('点击购买')




