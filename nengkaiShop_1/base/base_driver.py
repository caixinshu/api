from telnetlib import EC

# import js as js
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class ShopDriver(object):

    def __init__(self, browser):
        '''浏览器'''
        if browser == 'Firefox':
            driver = webdriver.Firefox()
            try:
                self.driver = driver
            except Exception:
                raise NameError('Firefox Not Found')
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            try:
                self.driver = driver
            except Exception:
                raise NameError('Chrome Not Found')

        else:
            print('Not Fount Browser !')


    def get_element(self,selector):
        '''定位元素'''
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0].strip()
        selector_value = selector.split(',')[1].strip()

        if selector_by == 'i' or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        else:
            raise  NameError('please enter a valid type of target element')

        return element

    # def add_cookie(self):
    #     '''添加单个cookie'''
    #     cookie_name = cookie_dict["name"]
    #     cookie_value = self.driver.get_cookie(cookie_name)
    #     if cookie_value is not None:
    #         self.driver.delete_cookie(cookie_name)
    #     self.driver.add_cookie(cookie_dict)

    def add_cookies(self,cookies):
        '''添加多个cookies'''
        self.driver.add_cookie(cookie_dict=cookies)

    def clear_cookies(self):
        '''清楚所有cookie'''
        self.driver.delete_all_cookies()

    def remove_cookie(self,name):
        '''删除指定name的cookie'''
        old_cookie_value = self.driver.get_cookie(name)
        if old_cookie_value is not None:
            self.driver.delete_cookie(name)

    def refresh(self,url=None):
        '''刷新页面'''
        if url is None:
            self.driver.refresh()
        else:
            self.driver.get(url)

    def type(self,selector,text):
        '''输入内容'''
        ele = self.get_element(selector)
        ele.clear()
        ele.send_keys(text)

    def click(self,selector):
        '''点击操作'''
        ele = self.get_element(selector)
        ele.click()

    def navigate(self,url):
        '''打开网页'''
        self.driver.get(url)

    def switch_to_frame(self,selector):
        '''进入iframe'''
        ele = self.get_element(selector)
        self.driver.switch_to_frame(ele)

    def switch_default_frame(self):
        '''退出到最外层'''
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        '''退出到上一层iframe'''
        self.driver.switch_to.parent_frame()

    def select_by_index(self,selector,num):
        '''以index方式选择下拉选项'''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_index(num)

    def select_by_value(self,selector,value):
        '''以value方式选择下拉选项'''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_value(value)

    def select_by_visible_text(self,selector,text):
        '''以text方式选择下拉选项'''
        ele = self.get_element(selector)
        select = Select(ele)
        select.select_by_visible_text(text)

    def accept_alert(self):
        '''确定alert框'''
        self.driver.switch_to.alert().accept()

    def dismiss_alert(self):
        '''取消alert框'''
        self.driver.switch_to.alert().dismiss()

    def current_window_handle(self):
        '''获取当前窗口句柄'''
        return self.driver.window_handle

    def window_handles(self):
        '''获取所有窗口句柄'''
        return self.driver.current_window_handles

    def open_new_window(self,selector):
        '''进入新窗口页面'''
        current_handle = self.driver.current_window_handle
        ele = self.get_element(selector)
        ele.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)

    def maximize_window(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def implicitly_wait(self,second):
        '''智能等待元素（作用域是全局）'''
        self.driver.implicitly_wait(second)

    def quit_browser(self):
        '''退出浏览器'''
        self.driver.quit()

    def sleep(self,time):
        '''休眠'''
        sleep(time)

    def get_url(self):
        '''获取当前页面url'''
        return self.driver.current_url

    def get_title(self):
        '''获取当前页面的标题'''
        return self.driver.title

    def get_text(self,selector):
        '''获取元素文本'''
        ele = self.get_element(selector)
        return ele.text

    def double_click(self,seletor):
        '''双击'''
        ele = self.get_element(seletor)
        ActionChains(self.driver).double_click(ele).perform()

    def get_screenshot(self,name):
        '''截图'''
        self.driver.get_screenshot_as_file('..\\screenshots\\%s_%s.png'
                                           %(time.strftime('%Y-%m-%d_%H-%M-%S'),name))

    def save_snapshot(self,file_name):
        '''保存图片'''
        self.driver.save_screenshot(file_name)

    def drag(self,source,target):
        '''拖拽'''
        ele = self.get_element(source)
        ele2 = self.get_element(target)
        # ActionChains(self.driver).click_and_hold(ele).release(ele2).perform()
        ActionChains(self.driver).drag_and_drop(ele,ele2).perform()

    def drag_js(self,selector):
        '''元素聚焦'''
        target = self.get_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def click_by_text(self,text):
        '''点击文字超链接'''
        self.get_element('p,' + text).click()

    def click_submit(self,selector):
        '''点击按钮'''
        ele = self.get_element(selector)
        ele.submit()

    def right_click(self,selector):
        '''鼠标右键'''
        ele = self.get_element(selector)
        ActionChains(self.driver).context_click(ele).perform()

    # def hover_mouse(self,selector):
    #     '''鼠标悬浮'''
    #     ele = self.get_element(selector)
    #     more_menu = WebDriverWait(driver=self.driver, timeout=15).until(
    #         EC.visibility_of_element_located(By.XPATH, ele))
    #     self.driver.execute_script(js, more_menu)
    #     time.sleep(3)

    def mouse(self,selector):
        ele = self.get_element(selector)
        ActionChains(self.driver).move_to_element(ele).perform()


if '__main__' == __name__:
    aa = ShopDriver('Chrome')

