#coding=utf-8
from selenium import webdriver
#富文本框的操作，不是textarea
dirver = webdriver.Firefox()
#dirver.get( "http://localhost:63342/studyselenium02/demo/textarea.html")
dirver.get( "http://www.vemmis.com/bjq/index.html")
dirver.implicitly_wait(5)
dirver.maximize_window()
content="ssssssssss"
js='document.getElementById("ueditor_0").contentWindow.document.body.innerHTML="%s"'%(content)
dirver.execute_script(js)
