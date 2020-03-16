from selenium import webdriver
from selenium.webdriver.common.by import By

from woniuBoss.lib.login import Login
from woniuBoss.tools.service import Service
login_data = {"username":"wncd000","password":"woniu123"}
driver = webdriver.Chrome()
driver.get("http://192.168.114.220:8080/WoniuBoss2.5/")
Login().do_login(driver,login_data)
driver.get("http://192.168.114.220:8080/WoniuBoss2.5/resource")
# 获取下拉列表中的内容
Service().get_select_values(driver,By.ID,"poolSelect")

# 除去
# Service.remove_readonly(driver,'date1')
ele =driver.find_element_by_id('date1')
ele.send_keys('2020-02-02')
driver.find_element_by_css_selector("div.pull-right>button.btn-primary").click()
driver.find_element_by_css_selector('input[name="cus.name"]').send_keys('hello')