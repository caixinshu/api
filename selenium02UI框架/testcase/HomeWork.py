# -*- coding:utf-8 -*-
import  random
#2、网址：https://reg.jd.com/reg/company
#完成一个注册功能，输出当前页面的title,输出当前页面源码，输出url,
#打印用户名，打印出联系人信息文本，获取当前页面的复选按钮的个数
#随机生成电话号码
def randomtelphone():
    telnum=random.choice(['139','188','185','136','158','151','186'])+"".join(random. sample ("0123456789",8 ))
    return telnum
#
# #随机生成一个字符串
def randomhs():
   hsnum="HS"+"".join(random.sample(u'撒大声地说的撒大声道',5))
   return hsnum
#随机生成一个姓名
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.maximize_window()
driver.get('https://reg.jd.com/reg/company')
driver.find_element_by_id('regName').send_keys(randomhs())
driver.find_element_by_id('pwd').send_keys('Azs19796342')
driver.find_element_by_id('pwdRepeat').send_keys('Azs19796342')
driver.find_element_by_id('companyname').send_keys(u'京东有限公司')
#driver.find_element_by_xpath(".//*[@id='companyprovince']").click()
driver.find_element_by_xpath(".//*[@id='companyprovince']/option[2]").click()
time.sleep(2)
#driver.find_element_by_xpath(".//*[@id='companycity']").click()
driver.find_element_by_xpath(".//*[@id='companycity']/option[2]").click()
time.sleep(2)
#driver.find_element_by_xpath(".//*[@id='companyarea']").click()
driver.find_element_by_xpath(".//*[@id='companyarea']/option[7]").click()
driver.find_element_by_id('companyaddr').send_keys(u'深圳市天亿冠丰科技有限公司')
inputid=driver.find_elements_by_id('purpose2')
for inputids in inputid:
    if inputids.get_attribute('type')=='checkbox' and inputids.is_selected()is False:
        inputids.click()
print inputids.is_selected()
driver.find_element_by_id('companysite').send_keys(randomtelphone())
#driver.find_element_by_xpath(".//*[@id='employees']").click()
driver.find_element_by_xpath(".//*[@id='employees']/option[4]").click()
#driver.find_element_by_xpath(".//*[@id='industry']").click()
driver.find_element_by_xpath(".//*[@id='industry']/option[5]").click()
#driver.find_element_by_xpath(".//*[@id='nature']").click()
driver.find_element_by_xpath(".//*[@id='nature']/option[7]").click()
driver.find_element_by_id('realname').send_keys(u'安志上')
#driver.find_element_by_xpath(".//*[@id='department']").click()
driver.find_element_by_xpath(".//*[@id='department']/option[5]").click()
driver.find_element_by_id('tel').send_keys('010-87726193')
driver.find_element_by_id('mobile').send_keys('13520225133')
driver.find_element_by_id('bsendMobileCode').click()
time.sleep(10)
#driver.find_element_by_id('bMobileCode').send_keys('556778')   问题：能否手动输入短信验证码
driver.find_element_by_id('mail').send_keys('anyueazs@sina.com')
time.sleep(10)
#driver.find_element_by_id('authcode').send_keys('3CVH')        问题：能否手动输入图片验证码
readme=driver.find_element_by_id('readme')
if readme.is_selected()=='False' and readme.get_attribute('type')=='checkbox':
    readme.click()
driver.find_element_by_id('registsubmit').click()
print driver.title   #输出当前页面的title
# print driver.page_source    #输出当前页面的源码
# print driver.current_url    #输出当前页面的url
# print driver.find_element_by_id('regName').get_attribute('value')   #打印用户名
# print driver.find_element_by_xpath(".//*[@id='formcompany']/div/h3[3]").text    #打印出联系人文本信息
# checkboxinputs=driver.find_elements_by_tag_name('input')
# checkbox=0
# for checkboxinput in checkboxinputs:
#     if checkboxinput.get_attribute('type')=='checkbox':
#         checkbox=checkbox+1
# print checkbox  #打印当前页面中的复选框按钮的个数
