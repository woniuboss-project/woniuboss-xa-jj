from selenium import webdriver
from selenium.webdriver.common.by import By

from woniuBoss.lib.login import Login
from woniuBoss.tools.service import Service
login_data = {"username":"wncd000","password":"woniu123"}
driver = webdriver.Chrome()
driver.get("http://192.168.114.220:8080/WoniuBoss2.5/")
Login().do_login(driver,login_data)
driver.get("http://192.168.114.220:8080/WoniuBoss2.5/resource")
Service().get_select_values(driver,By.ID,"poolSelect")
