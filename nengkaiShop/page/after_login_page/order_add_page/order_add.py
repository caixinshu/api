from base.base_page import BasePage

class OrderAdd(BasePage):



    '''订单页'''
    def first_order_info(self):
        '''添加地址信息'''
        driver = self.base_driver
        driver.type('n,rename','张珊珊')
        driver.click('x,/html/body/div[6]/div[1]/div[2]/ul/form/dl[2]/dd/span')
        driver.click_by_text('安徽')
        driver.click_by_text('合肥')
        driver.click_by_text('长丰县')
        driver.type('n,addr','长安街九乡6里8号')
        #driver,type('n,postcode','490000')
        driver.type('n,mobile','13823218582')
        driver.click('x,/html/body/div[6]/div[1]/div[2]/ul/form/button[1]')

    def del_order_info(self):
        '''删除地址信息'''
        driver = self.base_driver
        # driver.hover_mouse('x,/html/body/div[6]/div[1]/div[2]/ul/li/span[1]')
        driver.mouse('x,/html/body/div[6]/div[1]/div[2]/ul/li/span[1]')
        driver.click_by_text('删除')
        driver.sleep(5)
        driver.click('x,//*[@id="jquery-interactive-confirm"]/table/tbody/tr[2]/td[2]/div/div/div[5]/button[1]/span')


    def edit_order_info(self):
        '''编辑地址信息'''
        driver = self.base_driver
        # driver.hover_mouse('x,/html/body/div[6]/div[1]/div[2]/ul/li/span[1]')
        driver.mouse('x,/html/body/div[6]/div[1]/div[2]/ul/li/span[1]')
        driver.click_by_text('编辑')
        driver.sleep(5)
        driver.type('n,mobile', '13811111111')
        driver.click('x,//*[@id="address_content_form"]/ul/form/button[1]/span')

    def get_assertion_information(self):
        '''获取订单编号'''
        driver = self.base_driver
        text = driver.get_text('x,/html/body/div[2]/div[1]/div[1]/p[1]/span[4]')
        return text